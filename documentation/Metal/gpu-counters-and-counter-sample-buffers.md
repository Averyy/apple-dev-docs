# GPU Counters and Counter Sample Buffers

**Framework**: Metal

Retrieve runtime data from a GPU device by sampling one or more of its counters.

#### Overview

A GPU  ([`MTLCounter`](mtlcounter.md)) is typically a hardware feature that tracks a specific performance metric, such as timestamps before and after an important rendering stage. A  ([`MTLCounterSet`](mtlcounterset.md)) is a collection of related counters. A  ([`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md)) represents the memory where a GPU device stores the data for a specific counter set.

You can retrieve and inspect data from a GPU’s counter set with the following steps:

1. Inspect which GPU counter sets a GPU device supports (see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).
2. Make a counter sample buffer to store the data (see [`Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)).
3. Instruct the GPU to save the counter set data to the buffer during a pass or an immediate mode command (see [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md)).
4. Transform the counter set data into a standard type (see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md)).

If you’re sampling data from a timestamp counter set ([`timestamp`](mtlcommoncounterset/timestamp.md)), you may need to convert the timestamps from the GPU’s clock to the CPU’s clock. See [`Converting GPU Timestamps into CPU Time`](converting-gpu-timestamps-into-cpu-time.md) for more information.

## Topics

### Counters and Counter Sets
- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
  Check whether a GPU produces the runtime performance data you want to sample.
- [protocol MTLCounterSet](mtlcounterset.md)
  A collection of individual counters a GPU device supports for a counter set.
- [struct MTLCommonCounterSet](mtlcommoncounterset.md)
  The name of a specific counter set that a GPU device can support.
- [protocol MTLCounter](mtlcounter.md)
  An individual counter a GPU device lists within one of its counter sets.
- [struct MTLCommonCounter](mtlcommoncounter.md)
  The name of a specific counter that can appear in a GPU device’s counter sets.
### Counter Sample Buffers
- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [protocol MTLCounterSampleBuffer](mtlcountersamplebuffer.md)
  A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.
- [var MTLCounterDontSample: Int](mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.
### Counter Sample Data Output
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
  Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [struct MTLCounterResultTimestamp](mtlcounterresulttimestamp.md)
  The data structure for storing the data you resolve from a timestamp counter set.
- [struct MTLCounterResultStatistic](mtlcounterresultstatistic.md)
  The data structure for storing the data you resolve from a statistic counter set.
- [struct MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md)
  The data structure for storing the data you resolve from a stage-utilization counter set.
- [var MTLCounterErrorValue: UInt64](mtlcountererrorvalue.md)
  A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.
### Timestamp Data
- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
  Correlate GPU events with CPU timelines by calculating the CPU time equivalents for GPU timestamps.
- [typealias MTLTimestamp](mtltimestamp.md)
  The number of nanoseconds for a point in absolute time or Mach absolute time.
### Counter Sample Buffer Errors
- [struct MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.

## See Also

- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md)
  Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Capturing Metal Commands Programmatically](capturing-metal-commands-programmatically.md)
  Invoke Metal’s frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Logging shader debug messages](logging-shader-debug-messages.md)
  Print debugging messages that a shader generates using shader logging.
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
  Prototype and test your Metal apps in Simulator.
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
  Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Metal debugger](../Xcode/Metal-debugger.md)
  Debug and profile your Metal workload with a GPU trace.
- [Metal developer workflows](../Xcode/Metal-developer-workflows.md)
  Locate and fix issues related to your app’s use of the Metal API and GPU functions.
- [Metal Debugging Types](metal-debugging-types.md)
  Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/gpu-counters-and-counter-sample-buffers)*