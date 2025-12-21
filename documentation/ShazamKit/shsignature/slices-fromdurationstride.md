# slices(from:duration:stride:)

**Framework**: ShazamKit  
**Kind**: method

Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.

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
func slices(from start: TimeInterval, duration: TimeInterval, stride: TimeInterval? = nil) throws -> SHSignature.Slices
```

#### Return Value

A sequence from `start` of `duration` length. Each value in the sequence is separated by `stride`.

## Parameters

- `start`: The starting value to use for the sequence.
- `duration`: The desired duration of each sliced signature.
- `stride`: The amount to step by for each slice. Must be a non-zero positive value.

## See Also

- [SHSignature.Slices](shsignature/slices.md)
  A sequence of signature segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/slices(from:duration:stride:))*