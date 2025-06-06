# attributedString()

**Framework**: AppKit  
**Kind**: method

Returns an attributed string representing the receiver’s text storage.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func attributedString() -> NSAttributedString
```

#### Return Value

The attributed string of the receiver’s text storage.

#### Discussion

Implementation of this method is optional. A class adopting the `NSTextInputClient` protocol can implement this interface if it can be done efficiently to enable callers of this interface to access arbitrary portions of the receiver’s content more efficiently.

## See Also

- [func attributedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](nstextinputclient/attributedsubstring(forproposedrange:actualrange:).md)
  Returns an attributed string derived from the given range in the receiver’s text storage.
- [func insertText(Any, replacementRange: NSRange)](nstextinputclient/inserttext(_:replacementrange:).md)
  Inserts the given string into the receiver, replacing the specified content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/attributedstring())*