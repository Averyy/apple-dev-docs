# MTLCounterSet

**Framework**: Metal  
**Kind**: protocol

A collection of individual counters a GPU device supports for a counter set.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCounterSet : NSObjectProtocol
```

#### Overview

You can determine which counter sets a GPU supports by checking an [`MTLDevice`](mtldevice.md) instance’s [`counterSets`](mtldevice/countersets.md) property. A counter set’s [`name`](mtlcounterset/name.md) property typically matches one of the common counter set names that [`MTLCommonCounterSet`](mtlcommoncounterset.md) defines. Check whether a GPU device supports a specific counter by comparing elements of the [`counters`](mtlcounterset/counters.md) property with a counter’s common name that [`MTLCommonCounter`](mtlcommoncounter.md) defines.

> ❗ **Important**:  Some GPUs may only support some of the counters within a counter set.

 Some GPUs may only support some of the counters within a counter set.

For more information, see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Topics

### Identifying a Counter Set
- [var name: String](mtlcounterset/name.md)
  The name of the GPU’s counter set instance.
### Checking Which Counters a GPU Supports
- [var counters: [any MTLCounter]](mtlcounterset/counters.md)
  An array of the counter instances a GPU device supports.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
  Check whether a GPU produces the runtime performance data you want to sample.
- [struct MTLCommonCounterSet](mtlcommoncounterset.md)
  The name of a specific counter set that a GPU device can support.
- [protocol MTLCounter](mtlcounter.md)
  An individual counter a GPU device lists within one of its counter sets.
- [struct MTLCommonCounter](mtlcommoncounter.md)
  The name of a specific counter that can appear in a GPU device’s counter sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterset)*