# init(attributedSelectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithAttributedSelectedText:(NSAttributedString *) selectedText contextBefore:(NSAttributedString *) contextBefore contextAfter:(NSAttributedString *) contextAfter markedText:(NSAttributedString *) markedText selectedRangeInMarkedText:(NSRange) selectedRangeInMarkedText;
```

#### Discussion

The `attributedSelectedText`, `contextBefore`, and `contextAfter` parameters represent the same ranges as their counterparts in [`init(selectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)`](./init%28selectedtext,contextbefore,contextafter,markedtext,selectedrangeinmarkedtext%29.md), and carry the same requirements, with the addition of text formatting and style attributes.

## See Also

### Creating a text document context
- [init(selectedText: String?, contextBefore: String?, contextAfter: String?, markedText: String?, selectedRangeInMarkedText: NSRange)](./init%28selectedtext,contextbefore,contextafter,markedtext,selectedrangeinmarkedtext%29.md)
  Initializes a document with plain text strings that represent the selection and its surrounding context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext/init(attributedselectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:))*