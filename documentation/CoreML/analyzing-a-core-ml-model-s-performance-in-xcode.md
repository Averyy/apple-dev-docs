# Analyzing a Core ML model’s performance in Xcode

**Framework**: Core ML

Measure how your model runs on your Mac or a connected device by generating a performance report in Xcode.

#### Overview

A performance report lets you analyze a model’s speed and *compute unit* usage before you ever integrate it into your app. Xcode runs the model and reports how long it takes to load and make a prediction, and which compute unit (the Neural Engine, GPU, or CPU) runs each operation. This makes it easy to compare candidate models or architectures early on, without writing any app code.

Understanding where each operation runs also helps you reason about compute utilization in the context of your specific use case, or dig deeper into performance beyond what simple timers can tell you. A report covers timing and compute unit placement; it doesn’t measure memory or power use.

Use a performance report to:

- Confirm that each prediction finishes within the time you have for a single frame or interaction.
- See which compute unit runs each operation, so you can understand your model’s compute unit utilization and operation compatibility.
- Compare timings and placement across different devices or compute-unit configurations.

You generate a report on your Mac or a connected device, so the measurements reflect that specific hardware. Choose the device that matches where your app runs.

#### Open a Model in Xcode

You can open a model file, such as an `.mlpackage`, directly in Xcode by double-clicking it or choosing File > Open, without adding it to a project or a target. If the model is already part of an Xcode project, select it in the Project navigator instead. Either way, Xcode opens the model viewer, a tabbed editor for inspecting the model. Open its Performance tab, where you create and read reports.

![Screenshot of the model viewer in Xcode for a model named DepthAnythingV2SmallF16P6. The tab row shows General, Preview, Predictions, Performance, Structure, and Utilities, with Performance selected. The Performance pane reads, Create a Performance Report, and instructs you to click the + button in the bottom-left corner.](/images/com.apple.coreml/model-viewer-performance-tab@2x.png)

#### Create a Performance Report

The numbers in a report reflect what the device is doing while the report runs. Before you start, close other apps and nonessential processes on the device you’re testing. This helps ensure background work doesn’t affect the results.

Open the Performance tab and click the Add button (+) in the lower-left corner to create a report. Choose where to run it, either your Mac or a connected device, and choose a compute-unit configuration to test.

![Screenshot of the Choose a connected device dialog in Xcode. The dialog shows My Mac selected in the list of available devices, with Cancel and Next buttons.](/images/com.apple.coreml/coreml-performance-report-connected-devices@2x.png)

The configuration sets which compute units the model may use, such as All, CPU only, CPU and GPU, or CPU and Neural Engine. After you start the report, Xcode runs the model on the device and shows the report once it’s done; you don’t see intermediate results while it runs.

![Screenshot of the Choose compute unit dialog in Xcode. The Compute Unit options are All (selected), CPU only, CPU and GPU, and CPU and Neural Engine. The dialog has Cancel, Previous, and Run Test buttons.](/images/com.apple.coreml/performance-report-compute-unit@2x.png)

#### Read the Load and Prediction Times

A report shows three timings in milliseconds: prediction, load, and compilation. Load and compilation get the model ready to run; prediction is the cost of each individual prediction after that.

- ****Prediction is the repeated cost of how long a single prediction takes.****: This is usually the number to focus on, because the people who use your app feel it on every prediction. Compare it against the time your app can spend, such as your budget for each frame or each interaction. If it’s higher than that budget, optimize the model.
- ****Load is the time it takes to prepare a compiled model to run on the compute units you chose.****: Before a compiled model can be loaded it needs to be specialized for the OS version and compute units it runs on. An *uncached load* is one where specialization happens as part of that load; a *cached load* is one where specialization has already been cached by Core ML and it reuses the result. You don’t manage this caching yourself. The cache persists across loads, app launches and system reboots. However, the system purges the cache on an OS update or if the system needs to reclaim storage space on behalf of the user. Load isn’t always a one-time cost: some apps load the model once and reuse it, but others load it for each prediction, for example, if a feature only loads the model when someone picks an image and then makes one prediction. Watch the uncached load time for whichever pattern matches your app. If it’s high and your app loads the model repeatedly, consider loading it once and reusing it instead.
- ****Compilation is the one-time cost of turning the model into the form Core ML loads.****: Compilation takes an `.mlmodel` or `.mlpackage` and produces a `.mlmodelc` file (the compiled model that `MLModel` instances load from). Xcode compiles your app’s models when it builds your app, so it rarely affects what people experience. If your app downloads a model, compile it by calling [`compileModel(at:)`](mlmodel/compilemodel(at:)-45ao6.md), then examine the compile time in the report to see how long in-app compilation takes.

Each timing has a menu for the statistic to show across the runs: Average, First, Median, Minimum, Maximum, or Standard Deviation. By default it shows the median value (the middle value across the runs), so an unusually fast or slow run doesn’t skew it. From the same menu, choose Maximum or Standard Deviation to see how much a timing varies across runs.

Prediction has a First statistic: the cost of the very first prediction, which can be higher than later ones if it requires specialization specific to that input’s shape. Load’s other statistics, besides Uncached, all describe cached loads.

![Screenshot of the timings in an Xcode performance report. Compute Units Selected reads All (CPU, GPU, Neural Engine) and Prediction Function reads Default. Three tiles show Prediction at 22.93 ms, Load at 45.20 ms, and Compilation at 127.08 ms, each with a statistic menu set to Median.](/images/com.apple.coreml/performance-report-times@2x.png)

#### Read the Compute Unit for Each Operation

Below the timings, the report lists each operation in the model with a column for each compute unit: CPU, GPU, and Neural Engine. The Type column shows the kind of each operation, such as convolution or activation:

- A checked and filled diamond marks the unit that runs an operation.
- An unfilled and checked diamond marks a unit that could run it but doesn’t.
- A hollow diamond indicates the operation is incompatible with the corresponding unit or chosen configuration.

Hover over a diamond to see more detail about that compute unit.

![Screenshot of the Compute Unit Mapping in an Xcode performance report. A summary reads All: 764, CPU: 3, GPU: 21, Neural Engine: 740. A table lists operations with columns for number, name, type, estimated time in microseconds, CPU, GPU, and Neural Engine. Most rows show a checked and filled diamond in the Neural Engine column, and unfilled and checked diamonds in the CPU and GPU columns, meaning those units could run the operation but don’t. One row, var_80_cast_fp16, shows a checked and filled diamond in the CPU column, an unfilled and checked diamond in the GPU column, and a hollow diamond in the Neural Engine column, meaning the operation is incompatible with the Neural Engine.](/images/com.apple.coreml/performance-report-operations@2x.png)

Each operation indicates which units can run it, and the unit that ran the operation. These don’t always match. Core ML decides where each operation runs by weighing more than raw compute speed, including the cost of moving data between compute units and how long a compute unit takes to ramp up. As a result, an operation that’s compatible with the Neural Engine can still run on the CPU, when that’s the faster choice overall.

If a model’s performance or compute utilization isn’t aligned with your needs, you may need to change your model’s architecture or how it’s represented. That work is model optimization. For more information, watch the WWDC session [`Optimize your Core ML usage`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10027/). For a Python package you can use to convert and optimize models, download [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io/).

#### Compare Reports Across Devices and Configurations

Generate more than one report to compare. Xcode saves each report you generate in the Performance tab. Run the same model on your Mac and on a connected device to see where operations run on each, or run it with different compute-unit configurations to see how the timings and placement change. Comparing a run that uses all compute units against a CPU-only run, for example, shows how much the Neural Engine and GPU help your model.

Select two or more saved reports, then choose the table icon next to Open in Instruments to switch to a comparison view. It lines up the reports side by side under a common properties section, such as the model file name and device type, so you can see how their timings and compute-unit placement differ instead of switching between reports one at a time. This comparison view isn’t limited to reports for the same model. You can also export a report to save it and compare saved reports across different models.

![Screenshot of the comparison view in Xcode for two reports on My Mac, testing DepthAnythingV2SmallF16P6. Common properties list the model file name, model type, and device type. A table lists each report by its compute-unit configuration, CPU only and All (CPU, GPU, Neural Engine), with columns for Median Prediction, Median Load, and Median Compile in milliseconds. The CPU only row is selected and reads 54.49, 37.32, and 122.28; the All row reads 22.92, 45.76, and 124.20. An Export to CSV button appears above the table.](/images/com.apple.coreml/performance-report-comparison@2x.png)

For more fine-grained detail than the comparison view’s summary numbers, select a report and choose “Open in Instruments” to inspect it further. You can also select an operation and open the Structure tab for more information about that operation.

![Screenshot of the Compute Unit Mapping for a CPU Only report in Xcode. The summary reads All: 170, CPU: 170, GPU: 0, Neural Engine: 0. In the table, a checked and filled diamond in the CPU column marks each operation as running on the CPU, and the GPU and Neural Engine columns show hollow diamonds.](/images/com.apple.coreml/performance-report-cpu-only@2x.png)

Because this report was configured to use CPU only, the GPU and Neural Engine columns show hollow diamonds for every operation. That doesn’t mean these operations are incompatible with those units in general, only that they were incompatible with the specified configuration.

#### Read the Same Data in Code with a Compute Plan

A compute plan gives you the report’s compute-unit mapping in code. For each operation it tells you which compute devices can run it, which one Core ML uses, and an estimate of its relative cost. It doesn’t measure load or prediction times the way the report does. Use it when you want the placement and cost data without opening Xcode, like in a script or a build step.

```swift
// Compile your model, such as an `.mlpackage`, to get a compiled model URL.
let compiledModelURL = try await MLModel.compileModel(at: modelURL)

let configuration = MLModelConfiguration()
configuration.computeUnits = .all

let computePlan = try await MLComputePlan.load(
    contentsOf: compiledModelURL,
    configuration: configuration
)

guard case let .program(program) = computePlan.modelStructure,
      let mainFunction = program.functions["main"] else {
    return
}

for operation in mainFunction.block.operations {
    let usage = computePlan.deviceUsage(for: operation)
    let cost = computePlan.estimatedCost(of: operation)
    // usage?.supported: the compute devices that can run the operation.
    // usage?.preferred: the compute device Core ML runs it on.
    // cost?.weight: the operation's cost relative to others.
}
```

Load a compute plan with [`load(contentsOf:configuration:)`](mlcomputeplan-1w21n/load(contentsof:configuration:).md), which reads a compiled model, so compile an `.mlpackage` first with [`compileModel(at:)`](mlmodel/compilemodel(at:)-45ao6.md). Set [`computeUnits`](mlmodelconfiguration/computeunits.md) to the same configuration you test in the report. The plan’s model structure describes the model; for a machine learning program, read its `main` function and step through the operations in its block.

For each operation, [`deviceUsage(for:)`](mlcomputeplan-1w21n/deviceusage(for:).md) returns where it can run and [`estimatedCost(of:)`](mlcomputeplan-1w21n/estimatedcost(of:).md) returns its cost. These return values expose properties you read in code, not controls in Xcode: read [`supported`](mlcomputeplan-1w21n/deviceusage/supported.md) for the compute devices that can run the operation, [`preferred`](mlcomputeplan-1w21n/deviceusage/preferred.md) for the device Core ML runs it on, and [`weight`](mlcomputeplan-1w21n/cost/weight.md) to compare how expensive operations are relative to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-model-s-performance-in-xcode)*