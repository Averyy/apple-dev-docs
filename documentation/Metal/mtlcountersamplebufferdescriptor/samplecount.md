# sampleCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of instances of a counter set’s data that a counter sample buffer can store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: Int { get set }
```

```objc
@property (readwrite) NSUInteger sampleCount;
```

## Mentions

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](../creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)

## Discussion

The counter sample buffer instances you create with the [`MTLCounterSampleBufferDescriptor`](../mtlcountersamplebufferdescriptor.md) can store [`sampleCount`](./samplecount.md) instances of a counter set.

## See Also

### Configuring a descriptor for a counter sample buffer
- [var counterSet: (any MTLCounterSet)?](./counterset.md)
  A GPU device’s counter set instance that you want to sample.
- [var label: String](./label.md)
  The name for the counter sample buffer you create with the descriptor.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The memory storage mode for the counter sample buffers you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/samplecount)*