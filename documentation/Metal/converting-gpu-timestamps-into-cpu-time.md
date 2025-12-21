# Converting GPU timestamps into CPU time

**Framework**: Metal

Correlate GPU events with CPU timelines by calculating the CPU time equivalents for GPU timestamps.

#### Overview

Sampling runtime data from a GPU can provide a valuable insight to your app’s GPU performance (see [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md)). GPU timestamps in particular can isolate runtime issues by showing what the GPU is working on relative to what the CPU is doing. However, the timestamp values your app samples from a GPU don’t typically match a CPU’s timestamps because each uses different hardware to measure time. This means you can’t always compare GPU timestamps directly with CPU timestamps.

Your app can convert a GPU’s timestamps to CPU time by sampling both clocks at the same time to establish a common baseline of time. Establish that baseline by sampling both the GPU and CPU clocks at least twice. Typically, apps sample the timestamps at least twice, once before and once after the GPU stores its timestamp data in an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md). Your app needs the baseline to accurately convert the GPU’s timestamp data it  from a counter sample buffer. See [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md) for instructions about resolving data within a counter sample buffer.

##### Create a Reference Baseline in Time By Sampling the Cpu and Gpu Timestamps Twice

You can sample timestamps from the GPU and CPU at the same time by calling [`MTLDevice`](mtldevice.md) instance’s [`sampleTimestamps()`](mtldevice/sampletimestamps().md) method in Swift, or the [`sampleTimestamps:gpuTimestamp:`](mtldevice/sampletimestamps:gputimestamp:.md) method in Objective-C.

You can sample the initial timestamps any time before a pass, such as at launch time or when your app creates a command buffer.

> 💡 **Tip**:  Call [`sampleTimestamps()`](mtldevice/sampletimestamps().md) sparingly because doing so may trap to the kernel (to read the GPU clock), which can affect your app’s runtime performance.

Calculate the time span by sampling the GPU and CPU timestamps again after the command buffer completes.

The span of time establishes a baseline that your app needs to convert timestamps from a counter sample buffer into real-world time values.

> 💡 **Tip**:  One good strategy is to sample the timestamps when you create a command buffer, and again inside a completion handler for that command buffer.

For example, the code below samples the GPU and CPU timestamps before and immediately after the GPU runs the command buffer.

You can find implmentations for the methods that this code example refers to in this article, except for the `resolveSampleBuffer` method, which comes from an earlier article in this series, [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md).

##### Convert Gpu Timestamps to Cpu Time

Calculate the CPU time equivalent of a GPU timestamp by mathematically converting it using two sets of your app’s reference GPU and CPU timestamps.

> **Note**:  The system measures CPU timestamps in nanoseconds.

Convert a GPU timestamp by following these steps:

1. Subtract the GPU reference starting time from the GPU timestamp.
2. Divide the difference by the total GPU reference time span.
3. Multiply the product by the total CPU reference time span.
4. Add the starting CPU reference time.

The method returns a value in microseconds, but you can convert the value to a unit of time that you prefer.

Similarly, you can calculate the CPU time equivalent between two GPU timestamps by applying the latter calculations to the time span between them.

This method is useful to show the duration between the beginning and end of an event window. For example, you might use this to see the duration of the vertex and fragment stages of a render pass.

## See Also

- [typealias MTLTimestamp](mtltimestamp.md)
  The number of nanoseconds for a point in absolute time or Mach absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/converting-gpu-timestamps-into-cpu-time)*