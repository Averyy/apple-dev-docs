# label

**Framework**: Metal  
**Kind**: property

The name for the counter sample buffer you create with the descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var label: String { get set }
```

## See Also

- [var counterSet: (any MTLCounterSet)?](mtlcountersamplebufferdescriptor/counterset.md)
  A GPU device’s counter set instance that you want to sample.
- [var sampleCount: Int](mtlcountersamplebufferdescriptor/samplecount.md)
  The number of instances of a counter set’s data that a counter sample buffer can store.
- [var storageMode: MTLStorageMode](mtlcountersamplebufferdescriptor/storagemode.md)
  The memory storage mode for the counter sample buffers you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/label)*