# isValid(within:)

**Framework**: Swift  
**Kind**: method

Indicates whether the range set is valid for use with the provided attributed string.

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
func isValid(within text: some AttributedStringProtocol) -> Bool
```

#### Return Value

`true` when the range set is valid for use with the provided attributed string; otherwise, false. A range set is valid if each of its ranges are valid in the attributed string.

## Parameters

- `text`: An attributed string used to validate the range set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/isvalid(within:)-6u17e)*