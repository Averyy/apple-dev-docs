# SHSignature.Slices

**Framework**: ShazamKit  
**Kind**: struct  
**Role**: Structure

A sequence of signature segments.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Slices
```

## Topics

### Supporting types
- [SHSignature.Slices.Iterator](./slices/iterator.md)
  An iterator for asynchronously accessing signature slices.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Slicing signature segments
- [func slices(from: TimeInterval, duration: TimeInterval, stride: TimeInterval?) throws -> SHSignature.Slices](./slices%28from,duration,stride%29.md)
  Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/slices)*