# comparePositionInDecodeOrder(withPositionOf:)

**Framework**: AVFoundation  
**Kind**: method

Compares the relative positions of two sample cursors and returns their relative positions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func comparePositionInDecodeOrder(withPositionOf cursor: AVSampleCursor) -> ComparisonResult
```

#### Return Value

Returns a comparison result that indicates of this cursor points at a sample before, the same as, or after the sample pointed to by the specified cursor.

#### Discussion

Undefined results occur if this cursor and the passed in cursor reference different sequences of samples, such as when they’re created by different instances of [`AVAssetTrack`](avassettrack.md).

## Parameters

- `cursor`: An instance of   with which to compare positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/comparepositionindecodeorder(withpositionof:))*