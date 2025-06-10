# counters

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of the counter instances a GPU device supports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var counters: [any MTLCounter] { get }
```

## Mentions

- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)

#### Discussion

Check whether a GPU device supports a specific counter by comparing its common name (see [`MTLCommonCounter`](mtlcommoncounter.md)) with each element in the property’s array.

> ❗ **Important**:  Some GPUs may only support some of the counters within a counter set.

For more information, see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterset/counters)*