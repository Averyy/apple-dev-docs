# Inspecting, debugging, and profiling Core AI models

**Framework**: Core AI

Investigate model behavior, monitor activity, and profile performance using the Core AI tools across Xcode and the Core AI Debugger app.

#### Overview

Core AI provides three tools to help you investigate model behavior, monitor activity, and profile performance. Use them as needed while authoring a model, after integrating it, or when your app is running.

- [`Core AI Debugger`](https://developer.apple.comhttps://developer.apple.com/core-ai-debugger/): A standalone macOS app for inspecting model structure, running models, and validating inference against reference data.
- Core AI debug gauge: An Xcode feature that monitors model load, specialization, and inference activity in real time during a debug session.
- Core AI instrument: An Instruments template that profiles execution timing across the CPU, GPU, and Neural Engine.

The Core AI debug gauge and Core AI instrument focus on a model that’s already running inside your app. Core AI Debugger works directly with the `.aimodel` file and gives you a closer look when something the gauge or instrument flags needs deeper inspection. The tools share data, so a finding in one often leads to a closer look in another.

![A two-phase workflow diagram. In the Development phase, authoring and optimization sends reference data to Core AI Debugger and saves an .aimodel file. The .aimodel file provides numeric debug data to Core AI Debugger and integrates into an app in the Runtime phase. The app runs into the Core AI debug gauge, which captures data back to Core AI Debugger and captures a trace into the Core AI instrument. The app also profiles directly into the Core AI instrument.](https://docs-assets.developer.apple.com/published/dc31861e2e125ae16c5012eca31fc37e/core-ai-framework-overview-flow%402x.png)

For project setup, the Xcode model viewer, and how to load a model in your app, see [`Integrating on-device AI models in your app with Core AI`](integrating-on-device-ai-models-in-your-app-with-core-ai.md).

#### Inspect and Compare Model Files in Core Ai Debugger

Core AI Debugger is a standalone macOS app that you download from the [`Core AI Debugger`](https://developer.apple.comhttps://developer.apple.com/core-ai-debugger/) for working directly with `.aimodel` files. You can inspect a model’s operation graph, step through the source that produced each operation, and run the model against a connected device or your Mac.

The debugger also allows you to compare pairs of a model’s output against a reference run, helping you confirm whether a converted or optimized model still produces the results you expect.

See [`Inspecting Core AI models with Core AI Debugger`](inspecting-core-ai-models-with-core-ai-debugger.md) for inspection and execution, and [`Validating inference correctness against a reference run`](validating-inference-correctness-against-a-reference-run.md) for comparing a model against a reference run.

#### Perform Inference Checks with the Core Ai Debug Gauge

Built into Xcode, the Core AI debug gauge tracks each model load, specialization, and inference event in real time. Use it to confirm that your model loads when you expect it to, to spot unusually slow inference, or to find a specific event you want to investigate further. The Core AI debug gauge can hand a captured event off to Core AI Debugger for structural inspection, or to the Core AI instrument for deeper profiling.

For details, see [`Monitoring model performance with the debug gauge`](monitoring-model-performance-with-the-debug-gauge.md).

#### Analyze Model Performance with the Core Ai Instrument

The Core AI instrument is a template in Instruments that profiles your app’s Core AI activity with detailed timing across the CPU, GPU, and Neural Engine. Use it when you need detailed performance information, such as which compute units run your model, whether specialization happens when you expect, and how often your app reloads a model. The trace correlates Core AI events with hardware activity so you can see the full picture of execution.

For details, see [`Analyzing model runtime performance with Instruments`](analyzing-model-runtime-performance-with-instruments.md).

## Topics

### Runtime monitoring and analysis
- [Monitoring model performance with the debug gauge](monitoring-model-performance-with-the-debug-gauge.md)
  Track live inference activity and timing during a debug session.
- [Analyzing model runtime performance with Instruments](analyzing-model-runtime-performance-with-instruments.md)
  Diagnose model performance by capturing a trace in Instruments.
### Model inspection and validation
- [Inspecting Core AI models with Core AI Debugger](inspecting-core-ai-models-with-core-ai-debugger.md)
  Verify model correctness by inspecting the operations and comparing tensor outputs.
- [Validating inference correctness against a reference run](validating-inference-correctness-against-a-reference-run.md)
  Measure numerical divergence in a Core AI model against a reference run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models)*