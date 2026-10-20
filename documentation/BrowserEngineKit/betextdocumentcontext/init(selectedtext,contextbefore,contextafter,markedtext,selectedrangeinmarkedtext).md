# init(selectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)

**Framework**: BrowserEngineKit  
**Kind**: init

Initializes a document with plain text strings that represent the selection and its surrounding context.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
init(selectedText: String?, contextBefore: String?, contextAfter: String?, markedText: String?, selectedRangeInMarkedText: NSRange)
```

## Parameters

- `selectedText`: The currently selected text, or `nil` for a caret selection. Pass an empty string, not `nil`, when the selection consists of nontext — in that case, a single call to delete backward doesn’t remove content from the `contextBefore` parameter. This value can be empty if the selection falls outside the context’s area, even if selected text exists elsewhere in the document.
- `contextBefore`: A suffix of the text that precedes the selection, or `nil` if the selection is at the beginning of the document. This string needs to correspond to a range that contains no nontext content. If the string contains a number of backward-deletion repetitions, that same number of delete-backward calls needs to remove the corresponding text from the document. The string needs to begin on a word boundary, or outside of a word entirely.
- `contextAfter`: A prefix of the text that follows the selection, or `nil` if the selection is at the end of the document. This string needs to correspond to a range that contains no nontext content. The string needs to end on a word boundary, or outside of a word entirely.
- `markedText`: The current marked text, or `nil` if no marked text exists. This value can be empty if the marked text falls outside the context’s area, even if marked text exists elsewhere in the document.
- `selectedRangeInMarkedText`: The range of the current selection relative to the marked text range. Pass `(NSNotFound, 0)` to indicate no marked text.

## See Also

- [init(attributedSelectedText: NSAttributedString?, contextBefore: NSAttributedString?, contextAfter: NSAttributedString?, markedText: NSAttributedString?, selectedRangeInMarkedText: NSRange)](betextdocumentcontext/init(attributedselectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md)
  Initializes a document with attributed strings that represent the selection and its surrounding context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext/init(selectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:))*