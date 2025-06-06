# attributedSubstring(from:)

**Framework**: Foundation  
**Kind**: method

Returns an attributed string consisting of the characters and attributes within the specified range in the attributed string.

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
func attributedSubstring(from range: NSRange) -> NSAttributedString
```

#### Return Value

An `NSAttributedString` object consisting of the characters and attributes within `aRange` in the receiver.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters. This method treats the length of the string as a valid range value that returns an empty string.

## Parameters

- `range`: The range from which to create a new attributed string.   must lie within the bounds of the receiver.

## See Also

- [var string: String](nsattributedstring/string.md)
  The character contents of the attributed string as a string.
- [var length: Int](nsattributedstring/length.md)
  The length of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attributedsubstring(from:))*