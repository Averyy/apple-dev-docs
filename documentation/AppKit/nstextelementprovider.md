# NSTextElementProvider

**Framework**: AppKit  
**Kind**: protocol

A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextElementProvider : NSObjectProtocol
```

## Topics

### Accessing the range of the text element
- [var documentRange: NSTextRange](nstextelementprovider/documentrange.md)
  Describes the starting and ending locations for the document.
### Accessing and updating the text
- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](nstextelementprovider/enumeratetextelements(from:options:using:).md)
  Enumerates text elements starting at the text location you provide.
- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextelementprovider/location(_:offsetby:).md)
  Returns a new location from location with offset you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](nstextelementprovider/replacecontents(in:with:).md)
  Replaces the characters specified by range with the text elements you provide.
### Adjusting the range of the text element
- [func adjustedRange(from: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?](nstextelementprovider/adjustedrange(from:foreditingtextselection:).md)
  A method you implement if the location backing store requires manual adjustment after editing.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextelementprovider/offset(from:to:).md)
  Returns the offset between the two specified locations.
### Controlling synchronization with the backing store
- [func synchronizeToBackingStore((((any Error)?) -> Void)?)](nstextelementprovider/synchronizetobackingstore(_:).md)
  Synchronizes changes to the backing store.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextContentManager](nstextcontentmanager.md)
- [NSTextContentStorage](nstextcontentstorage.md)

## See Also

- [Enriching your text in text views](../UIKit/enriching-your-text-in-text-views.md)
  Add exclusion paths, text attachments, and text lists to your text, and render it with text views.
- [class NSTextParagraph](nstextparagraph.md)
  A class that represents a single paragraph backed by an attributed string as the contents.
- [class NSTextListElement](nstextlistelement.md)
  A class that represents a text list node.
- [class NSTextElement](nstextelement.md)
  An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider)*