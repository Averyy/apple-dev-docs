# Converting a GPU’s Counter Data into a Readable Format

**Framework**: Metal

Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.

#### Overview

To use the data a GPU driver stores in an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance (see [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md)), your app must  it. Resolving the data converts the counter data from the GPU’s internal data structure into a common format that Metal defines.

You can resolve the data in a counter sample buffer by creating a blit pass that converts the data as it copies it to an [`MTLBuffer`](mtlbuffer.md). If the CPU can access a counter sample buffer, you can also resolve the data after the GPU finishes running a command buffer. See [`Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) for information about making a CPU-accessible counter sample buffer.

##### Resolve the Counter Sample Buffer with the Cpu

For an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance that you create with shared memory (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md) and [`MTLStorageMode.shared`](mtlstoragemode/shared.md)), you can resolve the data by calling its [`resolveCounterRange(_:)`](mtlcountersamplebuffer/resolvecounterrange(_:).md) method.

You can resolve a sample counter buffer with the CPU at any time after the GPU finishes running the pass that retrieves the counter’s data. To access the data as soon as possible (with the CPU), add a completion handler to the pass’s command buffer by calling its [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method.

##### Resolve the Counter Sample Buffer with a Blit Pass on the Gpu

You can also resolve an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance’s data into an [`MTLBuffer`](mtlbuffer.md) by running a blit pass on the GPU. For some GPUs, this technique is the only way to resolve a counter sample buffer that uses private storage (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md) and [`MTLStorageMode.private`](mtlstoragemode/private.md)).

To resolve a sample counter buffer in a blit pass, create an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance and call its [`resolveCounters(_:range:destinationBuffer:destinationOffset:)`](mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:).md) method.

##### Cast the Counter Samples Data to a Result Type

Your app can inspect and use the resolved data by casting it to the result type that corresponds to the counter set.

| Counter set names | Counter result types |
| --- | --- |
| [`timestamp`](mtlcommoncounterset/timestamp.md) | [`MTLCounterResultTimestamp`](mtlcounterresulttimestamp.md) |
| [`stageUtilization`](mtlcommoncounterset/stageutilization.md) | [`MTLCounterResultStageUtilization`](mtlcounterresultstageutilization.md) |
| [`statistic`](mtlcommoncounterset/statistic.md) | [`MTLCounterResultStatistic`](mtlcounterresultstatistic.md) |

For example, your app can cast the data it resolves from a [`timestamp`](mtlcommoncounterset/timestamp.md) counter set as an [`MTLCounterResultTimestamp`](mtlcounterresulttimestamp.md) array.

The code example above also checks whether the result type array has the correct number of elements of the counter set for the app.

##### Inspect the Information and Check for Error Values

You can also use the result type instances to check whether the GPU stores any error values. The following code example determines whether any of the timestamp samples are equal to `0` or a sentinel error value:

Any time the GPU encounters a runtime error while sampling a counter, it sets the counter datum to the sentinel value [`MTLCounterErrorValue`](mtlcountererrorvalue.md).

> **Note**:  A GPU typically stores timestamp values from its internal clock. You can convert those timestamps into more meaningful time values, in nanoseconds, with [`sampleTimestamps()`](mtldevice/sampletimestamps().md) — see [`Converting GPU Timestamps into CPU Time`](converting-gpu-timestamps-into-cpu-time.md).

 A GPU typically stores timestamp values from its internal clock. You can convert those timestamps into more meaningful time values, in nanoseconds, with [`sampleTimestamps()`](mtldevice/sampletimestamps().md) — see [`Converting GPU Timestamps into CPU Time`](converting-gpu-timestamps-into-cpu-time.md).

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