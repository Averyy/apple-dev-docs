# extracting(droppingFirst:)

**Framework**: Swift  
**Kind**: method

Returns a span over all but the given number of initial bytes.

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
func extracting(droppingFirst k: Int) -> RawSpan
```

#### Return Value

A span starting after the specified number of bytes.

#### Discussion

If the number of elements to drop exceeds the number of bytes in the span, the result is an empty span.

The returned span’s first byte is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> **Note**: O(1)

## Parameters

- `k`: The number of bytes to drop from the beginning of   the span.   must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/extracting(droppingfirst:))*