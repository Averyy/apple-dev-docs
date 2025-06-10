# extracting(last:)

**Framework**: Swift  
**Kind**: method

Returns a span containing the final elements of the span, up to the given maximum length.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
mutating func extracting(last maxLength: Int) -> MutableSpan<Element>
```

#### Return Value

A span with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the length of this span, the result contains all the elements.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> **Note**: O(1)

## Parameters

- `maxLength`: The maximum number of elements to return.    must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/extracting(last:))*