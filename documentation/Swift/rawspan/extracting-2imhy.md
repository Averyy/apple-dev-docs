# extracting(_:)

**Framework**: Swift  
**Kind**: method

Constructs a new span over the bytes within the supplied range of positions within this span.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
func extracting(_ bounds: Range<Int>) -> RawSpan
```

#### Return Value

A span over the bytes within `bounds`

#### Discussion

The returned span’s first byte is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> **Note**: O(1)

## Parameters

- `bounds`: A valid range of positions. Every position in   this range must be within the bounds of this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/extracting(_:)-2imhy)*