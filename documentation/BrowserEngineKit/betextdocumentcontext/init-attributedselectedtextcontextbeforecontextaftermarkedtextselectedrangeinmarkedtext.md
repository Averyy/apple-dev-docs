# init(attributedSelectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)

**Framework**: BrowserEngineKit  
**Kind**: init

Initializes a document with attributed strings that represent the selection and its surrounding context.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
init(attributedSelectedText selectedText: NSAttributedString?, contextBefore: NSAttributedString?, contextAfter: NSAttributedString?, markedText: NSAttributedString?, selectedRangeInMarkedText: NSRange)
```

#### Discussion

The `attributedSelectedText`, `contextBefore`, and `contextAfter` parameters represent the same ranges as their counterparts in [`init(selectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)`](betextdocumentcontext/init(selectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md), and carry the same requirements, with the addition of text formatting and style attributes.

## See Also

- [init(selectedText: String?, contextBefore: String?, contextAfter: String?, markedText: String?, selectedRangeInMarkedText: NSRange)](betextdocumentcontext/init(selectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md)
  Initializes a document with plain text strings that represent the selection and its surrounding context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext/init(attributedselectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:))*