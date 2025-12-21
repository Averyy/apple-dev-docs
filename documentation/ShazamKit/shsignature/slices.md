# SHSignature.Slices

**Framework**: ShazamKit  
**Kind**: struct

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
- [SHSignature.Slices.Iterator](shsignature/slices/iterator.md)
  An iterator for asynchronously accessing signature slices.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func slices(from: TimeInterval, duration: TimeInterval, stride: TimeInterval?) throws -> SHSignature.Slices](shsignature/slices(from:duration:stride:).md)
  Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/slices)*