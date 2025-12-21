# isValid(within:)

**Framework**: Swift  
**Kind**: method

Indicates whether the range is valid for use with the provided discontiguous attributed string.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func isValid(within text: DiscontiguousAttributedSubstring) -> Bool
```

#### Return Value

`true` when the range is valid for use with the provided discontiguous attributed string; otherwise, false. A range is valid if its lower and upper bounds are each either valid in the discontiguous attributed string or equivalent to the string’s `endIndex`.

## Parameters

- `text`: A discontiguous attributed string used to validate the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/isvalid(within:)-8h4h8)*