# MTLCounter

**Framework**: Metal  
**Kind**: protocol

An individual counter a GPU device lists within one of its counter sets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCounter : NSObjectProtocol
```

#### Overview

You can determine which counters a GPU supports within a counter set (see [`MTLCounterSet`](mtlcounterset.md)) by checking the elements of its [`counters`](mtlcounterset/counters.md) property. A counter’s [`name`](mtlcounter/name.md) property typically matches one of the common counter set names that [`MTLCommonCounter`](mtlcommoncounter.md) defines. For more information, see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Topics

### Identifying a Counter
- [var name: String](mtlcounter/name.md)
  The name of a GPU’s counter instance.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
  Check whether a GPU produces the runtime performance data you want to sample.
- [protocol MTLCounterSet](mtlcounterset.md)
  A collection of individual counters a GPU device supports for a counter set.
- [struct MTLCommonCounterSet](mtlcommoncounterset.md)
  The name of a specific counter set that a GPU device can support.
- [struct MTLCommonCounter](mtlcommoncounter.md)
  The name of a specific counter that can appear in a GPU device’s counter sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounter)*