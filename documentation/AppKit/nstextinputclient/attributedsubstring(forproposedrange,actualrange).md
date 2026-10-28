# attributedSubstring(forProposedRange:actualRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an attributed string derived from the given range in the receiver’s text storage.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func attributedSubstring(forProposedRange range: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?
```

```objc
- (NSAttributedString *) attributedSubstringForProposedRange:(NSRange) range actualRange:(NSRangePointer) actualRange;
```

## Return Value

The string created from the given range. May return `nil`.

## Discussion

An implementation of this method should be prepared for `aRange` to be out of bounds. For example, the InkWell text input service can ask for the contents of the text input client that extends beyond the document’s range. In this case, you should return the intersection of the document’s range and `aRange`. If the location of `aRange` is completely outside of the document’s range, return `nil`.

## Parameters

- `range`: The range in the text storage from which to create the returned string.
- `actualRange`: The actual range of the returned string if it was adjusted, for example, to a grapheme cluster boundary or for performance or other reasons. `NULL` if range was not adjusted.

## See Also

### Storing text
- [func attributedString() -> NSAttributedString](./attributedstring%28%29.md)
  Returns an attributed string representing the receiver’s text storage.
- [func insertText(Any, replacementRange: NSRange)](./inserttext%28_,replacementrange%29.md)
  Inserts the given string into the receiver, replacing the specified content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/attributedsubstring(forproposedrange:actualrange:))*