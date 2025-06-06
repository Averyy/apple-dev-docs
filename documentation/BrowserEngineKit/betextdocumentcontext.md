# BETextDocumentContext

**Framework**: BrowserEngineKit  
**Kind**: class

Information about the text surrounding a selection in a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BETextDocumentContext
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

## Topics

### Creating a text document context
- [init(attributedSelectedText: NSAttributedString?, contextBefore: NSAttributedString?, contextAfter: NSAttributedString?, markedText: NSAttributedString?, selectedRangeInMarkedText: NSRange)](betextdocumentcontext/init(attributedselectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md)
  Initializes a new document context with attributed strings. The `selectedText`, `contextBefore`, and `contextAfter` represent the same ranges as they do in the `-initWithSelectedText:contextBefore:contextAfter:` initializer.
- [init(selectedText: String?, contextBefore: String?, contextAfter: String?, markedText: String?, selectedRangeInMarkedText: NSRange)](betextdocumentcontext/init(selectedtext:contextbefore:contextafter:markedtext:selectedrangeinmarkedtext:).md)
### Getting information about the selected range
- [var autocorrectedRanges: [NSValue]](betextdocumentcontext/autocorrectedranges.md)
  Array of `NSRange` values, relative to the full context string made by combining the `contextBefore`, `markedText` (or `selectedText` if the marked text is empty), and the `contextAfter`.
### Adding text rectangles
- [func addTextRect(CGRect, forCharacterRange: NSRange)](betextdocumentcontext/addtextrect(_:forcharacterrange:).md)
  Adds a text `rect` for the given character `range` The CGRects representing each character range are specified in -textInputView coordinates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
- [class BETextAlternatives](betextalternatives.md)
- [class BETextDocumentRequest](betextdocumentrequest.md)
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](betextreplacementoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext)*