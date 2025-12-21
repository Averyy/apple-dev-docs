# counterSet

**Framework**: Metal  
**Kind**: property

A GPU device’s counter set instance that you want to sample.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var counterSet: (any MTLCounterSet)? { get set }
```

#### Discussion

Assign this property to one of the counter sets in an [`MTLDevice`](mtldevice.md) instance’s [`counterSets`](mtldevice/countersets.md) property.

## See Also

- [var label: String](mtlcountersamplebufferdescriptor/label.md)
  The name for the counter sample buffer you create with the descriptor.
- [var sampleCount: Int](mtlcountersamplebufferdescriptor/samplecount.md)
  The number of instances of a counter set’s data that a counter sample buffer can store.
- [var storageMode: MTLStorageMode](mtlcountersamplebufferdescriptor/storagemode.md)
  The memory storage mode for the counter sample buffers you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/counterset)*