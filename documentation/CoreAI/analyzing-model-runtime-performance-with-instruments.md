# Analyzing model runtime performance with Instruments

**Framework**: Core AI

Diagnose model performance by capturing a trace in Instruments.

#### Overview

When a Core AI model runs on your device, many events happen internally that can significantly affect performance. To get useful performance information for apps with on-device models, profile your app in Instruments. This template helps you:

- Profile model performance alongside the rest of your app.
- Identify startup delays from models that aren’t specialized for the current hardware.
- Compare model performance across CPU, GPU, and Neural Engine.
- Find unnecessary delays from repeatedly loading uncached models.

#### Record a New Trace

Start with your Xcode project open and your device connected to your Mac. Next, select your app’s scheme and a run destination, then choose Product > Profile. In the Instruments template picker, select the Core AI template and click the Choose button.

![The Instruments template picker dialog with the Standard tab selected and the Core AI template highlighted in the grid. A description below the grid reads, “Core AI: Monitors an application’s machine learning activity executed through Core AI.” The Choose button in the bottom-right is highlighted.](https://docs-assets.developer.apple.com/published/9af389a5b39c0253ff6e2c00b98cf14a/instrument-template-picker%402x.png)

Alternatively, open Instruments and choose the Core AI template.

The Core AI template includes the following instruments:

- **Core AI**: Captures timing information for activity in the Core AI framework across all four event categories (Specialization, Load, Setup, and Inference).
- **Neural Engine**: Captures activity on the Neural Engine, so you can correlate Core AI events with the hardware that runs them.
- **GPU**: Captures and shows activity on the GPU during the trace.
- **Time Profiler**: Profiles running threads on all cores at regular intervals for all processes.

> **Note**: Profile on a real device for the most accurate performance data.

To begin recording the trace, click the Record button at the top left of the window. In your app, perform the actions that invoke your Core AI model so the trace captures the resulting events. When you finish, click the Record button again to stop recording.

> **Note**: For the most actionable results, run your app on its own. Other apps competing for CPU, GPU, or Neural Engine resources can distort the trace.

#### Review the Trace Recording

Now that you’ve recorded a trace, the Instruments timeline shows recorded data from each of the instruments in the Core AI template.

![An Instruments timeline view with time markers from 00:00 to 00:45 showing five stacked tracks. The top track is the Core AI instrument, expanded to reveal nested child rows for a model and its main function; its Activity track shows a thin green band of activity near the start of the recording and a large blue block of activity from roughly 35 to 50 seconds. Beneath it, the Neural Engine track shows a magenta band with sparse activity at the start and clustered marks during the later blue block. The GPU track, labeled M3 Max, displays a continuous magenta band across the entire timeline. The Time Profiler track, labeled CPU Usage, shows a CPU activity graph with peaks at the start and during the later block. The bottom track, an M3 Max Metal Device State track, shows a magenta band with a dark segment near the end of the timeline.](https://docs-assets.developer.apple.com/published/487f2777fc1d7486803d5b994505d971/instrument-activity-overview%402x.png)

The Core AI instrument divides model activity into multiple tracks. The top track shows all activity. Expand it to reveal a child track for each active model, and expand a model’s track to reveal a child track for each of its active functions.

> **Note**: The default function name is `main`.

Each colored band represents an event in one of the four event categories. Each category has different latency characteristics. The categories, in the order they typically appear, are:

- **Specialization**: Runtime specialization of the model for the target device architecture. Only appears for models that aren’t specialized ahead of time. Appears in green in the timeline.
- **Load**: Preparation of the model for loading into memory. Appears in cyan in the timeline.
- **Setup**: Preparation of the model before each inference. Appears in magenta in the timeline.
- **Inference**: A single, complete inference from the model. Appears in blue in the timeline.

Specialization events are often the most time-intensive operations during model runtime. Each model produces at most one Specialization event — none if the model is fully specialized for the device or already cached. You can learn more about specialization and how to optimize model performance in your app in [`Compiling Core AI models ahead of time`](compiling-core-ai-models-ahead-of-time.md) and [`Managing model specialization and caching`](managing-model-specialization-and-caching.md).

![A zoomed-in Instruments timeline view spanning about one second around 00:13. The Core AI instrument appears in the left sidebar, expanded to show a model and its main function. In the Activity track, a green Specialize event labeled Compile Asset, Specialize starts just after 00:13.000 and extends to roughly 00:13.800, with a nested Compile segment sub-event inside it.](https://docs-assets.developer.apple.com/published/57b28b72edc0abf9a415b71408c31642/instrument-activity-specialize%402x.png)

Next, brief Load events appear in the timeline. They occur only at the start of runtime, when your app first loads the model into memory. If you see frequent Load events during runtime, check that your app doesn’t reload models repeatedly.

![A zoomed-in Instruments timeline view spanning roughly 200 milliseconds around 00:13.700. The Core AI instrument appears in the left sidebar, expanded to show a model and its main function. In the Activity track, the tail end of the green Specialize event labeled Compile Asset, Specialize, with a nested Compile segment sub-event, ends at 00:13.830.681, immediately followed by a small cyan Load event labeled Load model::main (10.54 μs).](https://docs-assets.developer.apple.com/published/8b6d286a1fb533a606728412bb4f8dce/instrument-activity-load%402x.png)

Finally, brief Setup events appear in the timeline, and Inference events follow. A Setup event precedes each inference.

![A zoomed-in Instruments timeline view spanning about 10 milliseconds around 00:38.558. The Core AI instrument appears in the left sidebar, expanded to show a model and its main function. In the Activity track, a thin magenta Setup event labeled Setup for model::main (66.96 μs) with a nested Context.alloc (22.83 μs) sub-event is immediately followed by a large blue Inference event labeled Run main and Run streaming function func_19. Nested rows beneath show corresponding blue Inference events for the model and its main function.](https://docs-assets.developer.apple.com/published/06be7d00bf477bb86e809a2dbcbd8dbf/instrument-activity-setup%402x.png)

## See Also

- [Monitoring model performance with the debug gauge](monitoring-model-performance-with-the-debug-gauge.md)
  Track live inference activity and timing during a debug session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/analyzing-model-runtime-performance-with-instruments)*