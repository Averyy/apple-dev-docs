# Downsampler.DownStreamSequence

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An async sequence of down stream elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct DownStreamSequence
```

Available when `Input` conforms to `Sendable`.

## Topics

### Getting the count
- [var count: Int?](./downstreamsequence/count.md)
  The count of elements.
### Creating an iterator
- [Downsampler.DownStreamSequence.Iterator](./downstreamsequence/iterator.md)
  An async iterator of down stream sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [TemporalSequence](../temporalsequence.md)

## See Also

### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> Downsampler<Input>.DownStreamSequence](./applied%28to,eventhandler%29.md)
  Down samples the input sequence


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/downstreamsequence)*