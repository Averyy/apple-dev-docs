# autocorrectedRanges

**Framework**: BrowserEngineKit  
**Kind**: property

An array of ranges that identify text the system autocorrects, relative to the context string.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var autocorrectedRanges: [NSValue] { get set }
```

#### Discussion

The context string is the concatenation of the initializer parameters `contextBefore`, `markedText` (or `selectedText` when marked text is empty), and `contextAfter`. For more information, see [`init(attributedSelectedText:contextBefore:contextAfter:markedText:selectedRangeInMarkedText:)`](betextdocumentcontext/init(attributedselectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext/autocorrectedranges)*