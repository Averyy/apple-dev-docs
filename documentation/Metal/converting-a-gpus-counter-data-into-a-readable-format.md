# Converting a GPU’s counter data into a readable format

**Framework**: Metal

Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.

#### Overview

To use the data a GPU driver stores in an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance (see [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md)), your app needs to *resolve* it. Resolving the data converts the counter data from the GPU’s internal data structure into a common format that Metal defines.

You can resolve the data in a counter sample buffer by creating a blit pass that converts the data as it copies it to an [`MTLBuffer`](mtlbuffer.md). If the CPU can access a counter sample buffer, you can also resolve the data after the GPU finishes running a command buffer. See [`Creating a counter sample buffer to store a GPU’s counter data during a pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) for information about making a CPU-accessible counter sample buffer.

##### Resolve the Counter Sample Buffer with the Cpu

For an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance that you create with shared memory (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md) and [`MTLStorageMode.shared`](mtlstoragemode/shared.md)), you can resolve the data by calling its [`resolveCounterRange(_:)`](mtlcountersamplebuffer/resolvecounterrange(_:).md) method.

**Swift**:

```swift
/// Converts the contents of the counter sample buffer into an array of result timestamps.
func resolveSampleBuffer() {
    /// Represents the size of the counter sample buffer.
    let range = 0..<sampleCount

    // Convert the contents of the counter sample buffer into the standard data format.
    guard let data = try? counterSampleBuffer.resolveCounterRange(range) else {
        return
    }
    ...
}
```

**Objective-C**:

```objective-c
/// Converts the contents of the counter sample buffer into an array of result timestamps.
- (void) resolveSampleBuffer
{
    /// Represents the size of the counter sample buffer.
    NSRange range = NSMakeRange(0, self.sampleCount);

    // Convert the contents of the counter sample buffer into the standard data format.
    NSData* data = [self.counterSampleBuffer resolveCounterRange:range];
    if (nil == data) {
        return;
    }
    ...
}
```

You can resolve a sample counter buffer with the CPU at any time after the GPU finishes running the pass that retrieves the counter’s data. To access the data as soon as possible (with the CPU), add a completion handler to the pass’s command buffer by calling its [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method.

**Swift**:

```swift
commandBuffer.addCompletedHandler { commandBuffer in
    let timestamps = func resolveSampleBuffer() {
    ...
}
```

**Objective-C**:

```objective-c
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> _Nonnull commandBuffer) {
    [self resolveSampleBuffer];
    ...
}];
```

##### Resolve the Counter Sample Buffer with a Blit Pass on the Gpu

You can also resolve an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance’s data into an [`MTLBuffer`](mtlbuffer.md) by running a blit pass on the GPU. For some GPUs, this technique is the only way to resolve a counter sample buffer that uses private storage (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md) and [`MTLStorageMode.private`](mtlstoragemode/private.md)).

To resolve a sample counter buffer in a blit pass, create an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance and call its [`resolveCounters(_:range:destinationBuffer:destinationOffset:)`](mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:).md) method.

**Swift**:

```swift
func resolveSampleBuffer(_ sampleBuffer: MTLCounterSampleBuffer,
                         with blitEncoder: MTLBlitCommandEncoder,
                         toBufferWith resourceOptions: MTLResourceOptions) -> MTLBuffer? {

    let counterBufferLength = MemoryLayout<MTLCounterResultTimestamp>.size * sampleCount
    let counterDataBuffer = sampleBuffer.device.makeBuffer(length: counterBufferLength,
                                                           options: resourceOptions)

    guard let counterDataBuffer = counterDataBuffer else {
        return nil
    }

    let range = 0..<sampleCount
    blitEncoder.resolveCounters(sampleBuffer,
                                range: range,
                                destinationBuffer: counterDataBuffer,
                                destinationOffset: 0)

    if resourceOptions.contains(.storageModeManaged) {
        blitEncoder.synchronize(resource: counterDataBuffer)
    }

    return counterDataBuffer
}
```

**Objective-C**:

```objective-c
(id<MTLBuffer>) resolveSampleBuffer:(id<MTLCounterSampleBuffer>)sampleBuffer
                      withBlitEncoder:(id<MTLBlitCommandEncoder>)blitEncoder
              toBufferWithStorageMode:(MTLResourceOptions)storageMode
{
    NSUInteger counterBufferLength = self.sampleCount * sizeof(MTLCounterResultTimestamp);
    id<MTLBuffer> counterDataBuffer = [sampleBuffer.device newBufferWithLength: counterBufferLength
                                                                       options: storageMode];

    if (nil == counterDataBuffer) {
        return nil;
    }

    NSRange range = NSMakeRange(0, self.sampleCount);

    [blitEncoder resolveCounters:sampleBuffer
                         inRange:range
               destinationBuffer:counterDataBuffer
               destinationOffset:0];


    if (storageMode & MTLStorageModeManaged) {
        [blitEncoder synchronizeResource:counterDataBuffer];
    }

    return counterDataBuffer;
}
```

##### Cast the Counter Samples Data to a Result Type

Your app can inspect and use the resolved data by casting it to the result type that corresponds to the counter set.

| Counter set names | Counter result types |
| --- | --- |
| [`timestamp`](mtlcommoncounterset/timestamp.md) | [`MTLCounterResultTimestamp`](mtlcounterresulttimestamp.md) |
| [`stageUtilization`](mtlcommoncounterset/stageutilization.md) | [`MTLCounterResultStageUtilization`](mtlcounterresultstageutilization.md) |
| [`statistic`](mtlcommoncounterset/statistic.md) | [`MTLCounterResultStatistic`](mtlcounterresultstatistic.md) |

For example, your app can cast the data it resolves from a [`timestamp`](mtlcommoncounterset/timestamp.md) counter set as an [`MTLCounterResultTimestamp`](mtlcounterresulttimestamp.md) array.

**Swift**:

```swift
/// Converts the contents of the counter sample buffer into an array of result timestamps.
func resolveSampleBuffer() {
    ...
 
    // Convert the contents of the counter sample buffer into the standard data format.
    guard let data = try? counterSampleBuffer.resolveCounterRange(range) else {
        return
    }

    // Declare the destination type for the `Data` instance's contents.
    let timestampSamples: [MTLCounterResultTimestamp]

    // Cast the resolved data into an array of the counter's result type.
    timestampSamples = Array(unsafeUninitializedCapacity: sampleCount) { buffer, initializedCount in
        // Save the size for each counter result timestamp instance.
        let elementSize = MemoryLayout<MTLCounterResultTimestamp>.size

        // Copy the data's bytes into the array's unsafe mutable buffer pointer.
        let bytesCopied = data.copyBytes(to: buffer)

        // Calculate how many complete counter result timestamp elements the method copies.
        initializedCount = bytesCopied / elementSize
    }

    // Check whether the number of samples is correct.
    guard timestampSamples.count == sampleCount else {
        print("Only \(timestampSamples.count) out of \(sampleCount) timestamps resolved.");
        return
    }

    ...
}
```

**Objective-C**:

```objective-c
/// Converts the contents of the counter sample buffer into an array of result timestamps.
- (void) resolveSampleBuffer
    ...
 
    // Convert the contents of the counter sample buffer into the standard data format.
    NSData* data = [self.counterSampleBuffer resolveCounterRange:range];
    ...

    NSUInteger resolvedSampleCount = data.length / sizeof(MTLCounterResultTimestamp);
    if (resolvedSampleCount < sampleCount) {
        printf("Only %lui out of %ui timestamps resolved.", resolvedSampleCount, sampleCount);
        return;
    }

    // Cast the data's bytes property to the counter's result type.
    MTLCounterResultTimestamp* timestamps = (MTLCounterResultTimestamp *)(data.bytes);
    ...
}
```

The code example above also checks whether the result type array has the correct number of elements of the counter set for the app.

##### Inspect the Information and Check for Error Values

You can also use the result type instances to check whether the GPU stores any error values. The following code example determines whether any of the timestamp samples are equal to `0` or a sentinel error value:

**Swift**:

```swift
/// Converts the contents of the counter sample buffer into an array of result timestamps.
func resolveSampleBuffer() {
    ...

    for (index, sample) in timestampSamples.enumerated() {
        if sample.timestamp == MTLCounterErrorValue {
            print("Timestamp sample \(index + 1) (of \(sampleCount)) has an error value.")
            return
        }

        if sample.timestamp == 0 {
            print("Timestamp sample \(index + 1) (of \(sampleCount)) has a value of zero.")
            return
        }
    }

    ...
}

```

**Objective-C**:

```objective-c
/// Converts the contents of the counter sample buffer into an array of result timestamps.
- (void) resolveSampleBuffer
    ...
 
    // Cast the data's bytes property to the counter's result type.
    MTLCounterResultTimestamp* timestamps = (MTLCounterResultTimestamp *)(data.bytes);

    // Check for invalid values within the (resolved) data from the counter sample buffer.
    for (int index = 0; index < resolvedSampleCount; index++) {
        MTLTimestamp timestamp = timestamps[index].timestamp;

        if (timestamp == MTLCounterErrorValue) {
            printf("Timestamp sample #%di (of %ui) has an error value.", index + 1, sampleCount);
            return;
        }

        if (timestamp == 0) {
            printf("Timestamp sample #%di (of %ui) has a value of zero.", index + 1, sampleCount);
            return;
        }
    }

    ...
}
```

Any time the GPU encounters a runtime error while sampling a counter, it sets the counter datum to the sentinel value [`MTLCounterErrorValue`](mtlcountererrorvalue.md).

> **Note**:  A GPU typically stores timestamp values from its internal clock. You can convert those timestamps into more meaningful time values, in nanoseconds, with [`sampleTimestamps()`](mtldevice/sampletimestamps().md) — see [`Converting GPU timestamps into CPU time`](converting-gpu-timestamps-into-cpu-time.md).

## See Also

- [struct MTLCounterResultTimestamp](mtlcounterresulttimestamp.md)
  The data structure for storing the data you resolve from a timestamp counter set.
- [struct MTLCounterResultStatistic](mtlcounterresultstatistic.md)
  The data structure for storing the data you resolve from a statistic counter set.
- [struct MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md)
  The data structure for storing the data you resolve from a stage-utilization counter set.
- [var MTLCounterErrorValue: UInt64](mtlcountererrorvalue.md)
  A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/converting-a-gpus-counter-data-into-a-readable-format)*