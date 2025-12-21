# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the attributed string is equal to the specified string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to other: NSAttributedString) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the text and attributes in the current string and `otherString` are the same, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method performs a character-by-character comparison of the string and its attributes. The character and its attributes must be the same in both strings for the method to return [`true`](https://developer.apple.com/documentation/Swift/true). In attributed strings with many attributes, such a comparison is unlikely to yield an exact match [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `other`: The attributed string with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/isequal(to:))*