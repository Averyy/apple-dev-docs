# Converting GPU timestamps into CPU time

**Framework**: Metal

Correlate GPU events with CPU timelines by calculating the CPU time equivalents for GPU timestamps.

#### Overview

Sampling runtime data from a GPU can provide a valuable insight to your app’s GPU performance (see [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md)). GPU timestamps in particular can isolate runtime issues by showing what the GPU is working on relative to what the CPU is doing. However, the timestamp values your app samples from a GPU don’t typically match a CPU’s timestamps because each uses different hardware to measure time. This means you can’t always compare GPU timestamps directly with CPU timestamps.

Your app can convert a GPU’s timestamps to CPU time by sampling both clocks at the same time to establish a common baseline of time. Establish that baseline by sampling both the GPU and CPU clocks at least twice. Typically, apps sample the timestamps at least twice, once before and once after the GPU stores its timestamp data in an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md). Your app needs the baseline to accurately convert the GPU’s timestamp data it *resolves* from a counter sample buffer. See [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md) for instructions about resolving data within a counter sample buffer.

##### Create a Reference Baseline in Time By Sampling the Cpu and Gpu Timestamps Twice

You can sample timestamps from the GPU and CPU at the same time by calling [`MTLDevice`](mtldevice.md) instance’s [`sampleTimestamps()`](mtldevice/sampletimestamps().md) method in Swift, or the [`sampleTimestamps:gpuTimestamp:`](mtldevice/sampletimestamps:gputimestamp:.md) method in Objective-C.

**Swift**:

```swift
func updateStartTimes(_ device: MTLDevice) {
    // Save the current CPU and GPU times as a baseline.
    let startTimes = device.sampleTimestamps()
    let cpuStart = Double(startTimes.cpu)
    let gpuStart = Double(startTimes.gpu)

    self.cpuStart = cpuStart
    self.gpuStart = gpuStart
}
```

**Objective-C**:

```objective-c
- (void) updateStartTimesWithDevice:(id<MTLDevice>)device {
    // Save the current CPU and GPU times as a baseline.
    MTLTimestamp cpuStartTimestamp = 0;
    MTLTimestamp gpuStartTimestamp = 0;

    [device sampleTimestamps:&cpuStartTimestamp
                gpuTimestamp:&gpuStartTimestamp];

    self.cpuStart = (double)cpuStartTimestamp;
    self.gpuStart = (double)gpuStartTimestamp;
}
```

You can sample the initial timestamps any time before a pass, such as at launch time or when your app creates a command buffer.

> 💡 **Tip**:  Call [`sampleTimestamps()`](mtldevice/sampletimestamps().md) sparingly because doing so may trap to the kernel (to read the GPU clock), which can affect your app’s runtime performance.

Calculate the time span by sampling the GPU and CPU timestamps again after the command buffer completes.

**Swift**:

```swift
func updateFinalTimes(_ device: MTLDevice) {
    // Update the final times with the current CPU and GPU times.
    let finalTimes = device.sampleTimestamps()

    cpuTimeSpan = Double(finalTimes.cpu) - cpuStart
    gpuTimeSpan = Double(finalTimes.gpu) - gpuStart
}
```

**Objective-C**:

```objective-c
- (void) updateFinalTimesWithDevice:(id<MTLDevice>)device {
    // Update the final times with the current CPU and GPU times.
    MTLTimestamp cpuFinalTimestamp = 0;
    MTLTimestamp gpuFinalTimestamp = 0;

    [device sampleTimestamps:&cpuFinalTimestamp
                gpuTimestamp:&gpuFinalTimestamp];

    self.cpuTimeSpan = (double)cpuFinalTimestamp - self.cpuStart;
    self.gpuTimeSpan = (double)gpuFinalTimestamp - self.gpuStart;
}
```

The span of time establishes a baseline that your app needs to convert timestamps from a counter sample buffer into real-world time values.

> 💡 **Tip**:  One good strategy is to sample the timestamps when you create a command buffer, and again inside a completion handler for that command buffer.

For example, the code below samples the GPU and CPU timestamps before and immediately after the GPU runs the command buffer.

**Swift**:

```swift
func configureCommandBuffer(_ commandBuffer: MTLCommandBuffer, frame: Int) {
    guard frame.isMultiple(of: framePollingPeriod) && frame != 0 else {
        return
    }

    timeConverter.updateStartTimes(commandBuffer.device)

    commandBuffer.addCompletedHandler { commandBuffer in
        self.resolveSampleBuffer()
        self.timeConverter.updateFinalTimes(commandBuffer.device)
        self.printVertexAndFragmentDurations(frame)
    }
}
```

**Objective-C**:

```objective-c
- (void)  configureCommandBuffer:(id<MTLCommandBuffer>) commandBuffer
                           frame: (NSUInteger)frame;
{
    if (frame % self.framePollingPeriod != 0) {
        return;
    }

    [self.timeConverter updateStartTimesWithDevice:commandBuffer.device];

    [commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> _Nonnull commandBuffer) {
        [self resolveSampleBuffer];
        [self.timeConverter updateFinalTimesWithDevice:commandBuffer.device];
        [self printVertexAndFragmentDurationsForFrame:frame];
    }];
}
```

You can find implmentations for the methods that this code example refers to in this article, except for the `resolveSampleBuffer` method, which comes from an earlier article in this series, [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md).

##### Convert Gpu Timestamps to Cpu Time

Calculate the CPU time equivalent of a GPU timestamp by mathematically converting it using two sets of your app’s reference GPU and CPU timestamps.

> **Note**:  The system measures CPU timestamps in nanoseconds.

Convert a GPU timestamp by following these steps:

1. Subtract the GPU reference starting time from the GPU timestamp.
2. Divide the difference by the total GPU reference time span.
3. Multiply the product by the total CPU reference time span.
4. Add the starting CPU reference time.

**Swift**:

```swift
func absoluteTimeInMicroseconds(timestamp: MTLTimestamp) -> Double {
    guard ready else { return Double.nan }

    // Convert the GPU time to a value within the range [0.0, 1.0].
    let normalizedGpuTime = (Double(timestamp) - gpuStart) / gpuTimeSpan

    // Convert GPU time to CPU time.
    let nanoseconds = (normalizedGpuTime * cpuTimeSpan) + cpuStart

    let microseconds = nanoseconds / 1e3
    return microseconds
}
```

**Objective-C**:

```objective-c
- (double) absoluteTimeInMicroseconds:(MTLTimestamp) timestamp {
    // Convert the GPU time to a value within the range [0.0, 1.0].
    double normalizedGpuTime = ((double)timestamp - self.gpuStart);
    normalizedGpuTime /= self.gpuTimeSpan;

    // Convert GPU time to CPU time.
    double nanoseconds = (normalizedGpuTime * self.cpuTimeSpan);
    nanoseconds += self.cpuStart;

    double microseconds = nanoseconds / 1000.0;
    return microseconds;
}
```

The method returns a value in microseconds, but you can convert the value to a unit of time that you prefer.

Similarly, you can calculate the CPU time equivalent between two GPU timestamps by applying the latter calculations to the time span between them.

**Swift**:

```swift
func microsecondsBetween(begin: MTLTimestamp, end: MTLTimestamp) -> Double {
    let timeSpan = Double(end) - Double(begin)

    // Convert GPU time to CPU time.
    let nanoseconds = timeSpan / gpuTimeSpan * cpuTimeSpan

    let microseconds = nanoseconds / 1e3
    return microseconds
}
```

**Objective-C**:

```objective-c
- (double) microsecondsBetweenBegin:(MTLTimestamp)begin
                                end:(MTLTimestamp)end {
    double timeSpan = (double)end - (double)begin;

    // Convert GPU time to CPU time.
    double nanoseconds = timeSpan / self.gpuTimeSpan * self.cpuTimeSpan;

    double microseconds = nanoseconds / 1000.0;
    return microseconds;
}
```

This method is useful to show the duration between the beginning and end of an event window. For example, you might use this to see the duration of the vertex and fragment stages of a render pass.

**Swift**:

```swift
func printVertexAndFragmentDurations(_ frame: Int) {
    guard let timestamps = resolvedTimestampSamples else { return }

    print("\n--- Frame \(frame) ---")

    if timestamps.count >= 2 {
        let vertexStart = timestamps[0].timestamp
        let vertexFinish = timestamps[1].timestamp

        let vertexTime = timeConverter.microsecondsBetween(begin: vertexStart,
                                                           end: vertexFinish)

        let roundedTime = String(format: "%.2f", vertexTime)
        print("    Vertex duration:   \(roundedTime) µS")
    }

    if timestamps.count >= 4 {
        let fragmentStart = timestamps[2].timestamp
        let fragmentFinish = timestamps[3].timestamp

        let fragmentTime = timeConverter.microsecondsBetween(begin: fragmentStart,
                                                             end: fragmentFinish)

        let roundedTime = String(format: "%.2f", fragmentTime)
        print("    Fragment duration: \(roundedTime) µS")
    }
}

```

**Objective-C**:

```objective-c
- (void) printVertexAndFragmentDurationsForFrame:(NSUInteger)frame
{
    if (nil == self.resolvedTimestampSamples) { return; }

    printf("\n--- Frame %lu ---\n", frame);

    if (self.resolvedTimestampSampleCount >= 2) {
        MTLTimestamp vertexStart = self.resolvedTimestampSamples[0].timestamp;
        MTLTimestamp vertexFinish = self.resolvedTimestampSamples[1].timestamp;

        printf("VS %.2llu\n", vertexStart);
        printf("VF %.2llu\n", vertexFinish);

        double vertexTime;
        vertexTime = [self.timeConverter microsecondsBetweenBegin:vertexStart
                                                              end:vertexFinish];

        printf("    Vertex duration:   %.2f µS\n", vertexTime);
    }

    if (self.resolvedTimestampSampleCount >= 4) {
        MTLTimestamp fragmentStart = self.resolvedTimestampSamples[2].timestamp;
        MTLTimestamp fragmentFinish = self.resolvedTimestampSamples[3].timestamp;

        double fragmentTime;
        fragmentTime = [self.timeConverter microsecondsBetweenBegin:fragmentStart
                                                                end:fragmentFinish];

        printf("    Fragment duration: %.2f µS\n", fragmentTime);
    }
}
```

## See Also

- [typealias MTLTimestamp](mtltimestamp.md)
  The number of nanoseconds for a point in absolute time or Mach absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/converting-gpu-timestamps-into-cpu-time)*