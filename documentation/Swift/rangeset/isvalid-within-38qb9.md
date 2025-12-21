# isValid(within:)

**Framework**: Swift  
**Kind**: method

Indicates whether the range set is valid for use with the provided discontiguous attributed string.

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

`true` when the range set is valid for use with the provided discontiguous attributed string; otherwise, false. A range set is valid if each of its ranges are valid in the discontiguous attributed string.

## Parameters

- `text`: A discontigious attributed string used to validate the range set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/isvalid(within:)-38qb9)*