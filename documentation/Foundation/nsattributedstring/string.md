# string

**Framework**: Foundation  
**Kind**: property

The character contents of the attributed string as a string.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var string: String { get }
```

#### Discussion

Attachment characters are not removed from the value of this property.

For performance reasons, this property returns the current backing store of the attributed string object. If you want to maintain a snapshot of this as you manipulate the returned string, you should make a copy of the appropriate substring.

This primitive property must guarantee efficient access to an attributed string’s characters; subclasses should implement it to execute in O(1) time.

## See Also

- [var length: Int](nsattributedstring/length.md)
  The length of the attributed string.
- [func attributedSubstring(from: NSRange) -> NSAttributedString](nsattributedstring/attributedsubstring(from:).md)
  Returns an attributed string consisting of the characters and attributes within the specified range in the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/string)*