# isValid(within:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the index is valid for use with the provided discontiguous attributed string.

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

`true` when the index is valid for use with the provided discontiguous attributed string; otherwise, false. An index is valid if it is both within the bounds of the discontigous attributed string and was produced from the provided string without any intermediate mutations.

## Parameters

- `text`: A discontiguous attributed string used to validate the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/index/isvalid(within:)-6wjr6)*