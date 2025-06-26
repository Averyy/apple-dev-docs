# isValid(within:)

**Framework**: Swift  
**Kind**: method

Indicates whether the range is valid for use with the provided discontiguous attributed string.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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