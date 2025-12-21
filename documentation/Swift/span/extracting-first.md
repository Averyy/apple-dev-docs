# extracting(first:)

**Framework**: Swift  
**Kind**: method

Returns a span containing the initial elements of this span, up to the specified maximum length.

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
func extracting(first maxLength: Int) -> Span<Element>
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/extracting(first:))*