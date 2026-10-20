# BETextDocumentContext

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface BETextDocumentContext : NSObject
```

## Mentions

- [Integrating custom browser text views with UIKit](./integrating-custom-browser-text-views-with-uikit.md)

#### Overview

The [`BETextInput`](./betextinput.md) protocol’s [`requestDocumentContext(_:completionHandler:)`](./betextinput/requestdocumentcontext%28_,completionhandler%29.md) and [`requestTextContextForAutocorrection(completionHandler:)`](./betextinput/requesttextcontextforautocorrection%28completionhandler%29.md) methods provide an instance of this class to their completion handlers.

## Topics

### Creating a text document context
- [init(attributedSelectedText: NSAttributedString?, contextBefore: NSAttributedString?, contextAfter: NSAttributedString?, markedText: NSAttributedString?, selectedRangeInMarkedText: NSRange)](./betextdocumentcontext/init%28attributedselectedtext,contextbefore,contextafter,markedtext,selectedrangeinmarkedtext%29.md)
  Initializes a document with attributed strings that represent the selection and its surrounding context.
- [init(selectedText: String?, contextBefore: String?, contextAfter: String?, markedText: String?, selectedRangeInMarkedText: NSRange)](./betextdocumentcontext/init%28selectedtext,contextbefore,contextafter,markedtext,selectedrangeinmarkedtext%29.md)
  Initializes a document with plain text strings that represent the selection and its surrounding context.
### Accessing autocorrected ranges
- [var autocorrectedRanges: [NSValue]](./betextdocumentcontext/autocorrectedranges.md)
  An array of ranges that identify text the system autocorrects, relative to the context string.
### Adding text rectangles
- [func addTextRect(CGRect, forCharacterRange: NSRange)](./betextdocumentcontext/addtextrect%28_,forcharacterrange%29.md)
  Adds a rectangle that corresponds to the specified character range in the document.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Replacements and AutoFill
- [class BEAutoFillTextSuggestion](./beautofilltextsuggestion.md)
  A suggestion object that provides AutoFill text content for web form fields based on a person’s usage patterns.
- [class BETextAlternatives](./betextalternatives.md)
  An object that provides alternative text suggestions for a person’s text selection.
- [class BETextDocumentRequest](./betextdocumentrequest.md)
  A description of the contextual information that a text document request retrieves.
- [BETextDocumentRequest.Options](./betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.
- [class BETextSuggestion](./betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](./betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext)*