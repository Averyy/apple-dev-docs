# init(startPoint:segments:)

**Framework**: PHASE  
**Kind**: init

Creates an envelope with a start point and segments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init?(startPoint: simd_double2, segments: [PHASEEnvelopeSegment])
```

#### Discussion

For an empty `segments` argument, the resulting envelope contains one segment where the end point matches the start point. If the `segments` argument contains more than one segment, the resulting [`segments`](phaseenvelope/segments.md) array sorts in ascending order on the  value.

> ❗ **Important**:  The start point’s  value must be less than or equal to the segment with the lowest  value of all other `segments`, otherwise this function returns `nil`.

## Parameters

- `startPoint`: The start point of the envelope.
- `segments`: An array of segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/init(startpoint:segments:))*