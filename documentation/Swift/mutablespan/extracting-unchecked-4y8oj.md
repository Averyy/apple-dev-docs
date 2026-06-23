# extracting(unchecked:)

**Framework**: Swift  
**Kind**: method

Constructs a new span over the items within the supplied range of indices within this span.

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
mutating func extracting(unchecked bounds: ClosedRange<MutableSpan<Element>.Index>) -> MutableSpan<Element>
```

#### Return Value

A `MutableSpan` over the items within `bounds`.

#### Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

This function does not validate `bounds`; this is an unsafe operation.

> **Note**: O(1)

## Parameters

- `bounds`: A valid range of indices. Every index in this range must be within the bounds of this `MutableSpan`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/extracting(unchecked:)-4y8oj)*