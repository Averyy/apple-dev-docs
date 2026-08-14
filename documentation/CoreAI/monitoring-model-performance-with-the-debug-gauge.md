# Monitoring model performance with the debug gauge

**Framework**: Core AI

Track live inference activity and timing during a debug session.

#### Overview

Use the Core AI debug gauge to monitor your Core AI model’s inference activity and performance in real time during a debug session. As your app runs, the gauge tracks inference, load, and specialization events. This helps you spot unexpected behavior and investigate individual events. For example, if your app uses an image classifier and you notice a misclassification during testing, find the corresponding Inference event in the gauge and capture its input values for further analysis.

![The Core AI gauge report page open in Xcode, with the Debug navigator on the left and, on the right, the Inference, Load, and Specialization metrics, three stacked activity graphs over a one-minute window, and the Activity table listing recorded events.](/images/com.apple.coreai/debug-gauge-report@2x.png)

To use the debug gauge, you need an Xcode project that uses at least one Core AI model. For more information on setting up a Core AI project, see [`Integrating on-device AI models in your app with Core AI`](integrating-on-device-ai-models-in-your-app-with-core-ai.md).

> **Note**: The gauge only appears in projects that link the [`Core AI`](CoreAI.md) framework. The gauge does not support the [`Core ML`](https://developer.apple.com/documentation/coreml) framework.

#### Open the Debug Gauge in Xcode

With your Xcode project open, build and run the project. In Debug navigator, you’ll see gauges such as CPU, Memory, Energy Impact, and the Core AI gauge.

![The Debug navigator listing the Core AI gauge alongside the CPU, Memory, Energy Impact, Disk, and Network gauges, with the Core AI row showing 0 µs/event before any inference runs.](/images/com.apple.coreai/debug-navigator@2x.png)

If you don’t see the gauge, verify that your project directly links the Core AI framework. To check, go to your project settings in the Xcode Navigator and scroll to Frameworks, Libraries, and Embedded Content in the General section. If you don’t see the Core AI framework, add it, then build and run your project again.

![The General tab of an Xcode target’s settings, with the Frameworks, Libraries, and Embedded Content section showing CoreAI.framework set to Always Used.](/images/com.apple.coreai/xcode-project-settings-core-ai-framework@2x.png)

#### Inspect Model Activity

With your app running and the Core AI debug gauge open, you can monitor and inspect any activity coming from your Core AI models. Run your model in your app, then look at the Core AI tray in the Debug Navigator. Vertical bars appear in the graph, where each bar represents the combined Core AI events that occur within a one-second interval. The horizontal axis shows time and the vertical axis shows the total duration of each combined event. Next to the bars, a label summarizes the median duration across all events combined.

![The Core AI row selected in the Debug navigator, showing a sparkline of recorded events and the label 10 ms per event next to a partial view of the report’s Inference panel.](/images/com.apple.coreai/debug-gauge-tray@2x.png)

You can open the gauge’s report page by clicking the Core AI tray in the Debug Navigator. Here, you see live, detailed information about the Core AI activity from your app. At the top, three separate metrics show the median duration for each event type:

- Inference: A single, complete inference from the model. Primary event type. Appears in blue in both the metrics and graph.
- Load: Preparation of the model for loading into memory. Appears in green in both the metrics and graph.
- Specialization: Runtime specialization of the model for the target device architecture. This only appears for models that aren’t specialized ahead of time. Appears in orange in both the metrics and graph.

#### Analyze Model Activity with the Activity Graphs and Table

As the debug gauge records Core AI activity from your app, you can watch the resulting Inference, Load, and Specialization events appear in each of the three graphs.

![Three stacked activity graphs in the report page, one each for Inference in blue, Load in green, and Specialization in orange, plotted on a shared one-minute timeline, with High, Low, and Count statistics labeled to the left of each graph.](/images/com.apple.coreai/debug-gauge-chart@2x.png)

Each graph displays data for a single event type. Each bar represents the maximum activity duration within a one-second interval. The horizontal axis shows time elapsed during the debug session. The vertical axis shows event duration.

Alongside each graph, you see metrics collected for each type of event. The metrics are:

- High: Maximum event duration.
- Low: Minimum event duration.
- Count: Number of events.

You can also examine the individual events with additional information in the Activity table below the activity graph. The table shows events from oldest to newest. Scroll to the bottom to turn on automatic scrolling, which always shows the latest events. To examine a specific row, scroll up to turn off automatic scrolling.

![The Activity table with Start, Duration, Model, and Event columns, listing a sequence of Load, Specialization, and Inference events recorded for the MobileNetV3ClassifierFP16 model.](/images/com.apple.coreai/debug-gauge-table@2x.png)

The activity graphs and the table are interactive. For example, if you notice a bar with an unexpected duration, click it, and the table selects the corresponding events. You can then see detailed information about those events in the table rows. You can also select events in the table, and the charts highlight the corresponding bars.

The table displays the following columns:

- Start: Start time of the event. Uses `hh:mm:ss.sss` format, relative to start time of first event received.
- Duration: Total duration of event. Units change dynamically depending on time scale.
- Model: Name of the model that produced the event. Matches the model’s filename.
- Event: Type of event. Either a Load, Inference, or Specialization event.

When you notice incorrect output from your model in your app, use the gauge to investigate the specific Inference event that produced it. Find the row for the corresponding Inference event in the Activity table, then click the More button to the right of the row.

![The More button context menu next to a row in the Activity table, showing two options: Open in DebugML… and Export to file….](/images/com.apple.coreai/debug-gauge-more-menu@2x.png)

The options available are:

- Open in Core AI Debugger: Opens the external [`Core AI Debugger`](https://developer.apple.comhttps://developer.apple.com/core-ai-debugger/) to inspect model structure and intermediate values.
- Export to file: Saves the input values for this inference to a file for later inspection.

> **Note**: Open the report page before triggering the event you want to investigate. The More button options aren’t available for events recorded before the report was open.

#### Record Performance Data

The debug gauge provides a quick, high-level view of the activity coming from the Core AI models in your app. Use the Core AI instrument in Instruments to record profiling data, compare it with other sources like Neural Engine or GPU activity, or examine Core AI events in more detail.

Start profiling in Instruments by clicking the Profile in Instruments button in the top-right corner of the gauge’s report page.

![The Profile in Instruments button in the top-right corner of the Core AI gauge report page header.](/images/com.apple.coreai/debug-gauge-instruments-button@2x.png)

Read [`Analyzing model runtime performance with Instruments`](analyzing-model-runtime-performance-with-instruments.md) for more details on the Core AI instrument.

#### Inspect a Specific Event Further

The debug gauge provides the only entry point to a live Core AI Debugger session, and the only way to capture the input tensors that produced a specific Inference event. After clicking the More button on a row in the Activity table, choose the option you need.

Choose Open in Core AI Debugger to start a Debugger session for the selected event. Core AI Debugger is a separate developer tool that visualizes a model’s structure and shows intermediate values throughout each operation. For more information, see [`Inspecting Core AI models with Core AI Debugger`](inspecting-core-ai-models-with-core-ai-debugger.md).

Choose Export to file to save the input tensors for the selected Inference event. A save dialog appears, letting you choose where to store the file. Single-tensor inputs save as `.npy` files; multi-tensor inputs save as zipped `.npz` files.

## See Also

- [Analyzing model runtime performance with Instruments](analyzing-model-runtime-performance-with-instruments.md)
  Diagnose model performance by capturing a trace in Instruments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/monitoring-model-performance-with-the-debug-gauge)*