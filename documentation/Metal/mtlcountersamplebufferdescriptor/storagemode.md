# storageMode

**Framework**: Metal  
**Kind**: property

The memory storage mode for the counter sample buffers you create with the descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var storageMode: MTLStorageMode { get set }
```

## Mentions

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)

#### Discussion

To access a counter sample buffer with the CPU, set this property to [`MTLStorageMode.shared`](mtlstoragemode/shared.md), otherwise [`MTLStorageMode.private`](mtlstoragemode/private.md).

## See Also

- [var counterSet: (any MTLCounterSet)?](mtlcountersamplebufferdescriptor/counterset.md)
  A GPU device’s counter set instance that you want to sample.
- [var label: String](mtlcountersamplebufferdescriptor/label.md)
  The name for the counter sample buffer you create with the descriptor.
- [var sampleCount: Int](mtlcountersamplebufferdescriptor/samplecount.md)
  The number of instances of a counter set’s data that a counter sample buffer can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/storagemode)*