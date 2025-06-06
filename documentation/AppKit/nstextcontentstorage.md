# NSTextContentStorage

**Framework**: AppKit  
**Kind**: class

A concrete object for managing your view’s text content and generating the text elements necessary for layout.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextContentStorage
```

#### Overview

An [`NSTextContentStorage`](nstextcontentstorage.md) object provides the backing store for a view that contains text. This object stores the text in an attributed string object, and defaults to using an [`NSTextStorage`](nstextstorage.md) object. It also maps portions of the text to [`NSTextElement`](nstextelement.md) objects to organize the text into paragraphs, lists, and other common element types found in text content. During layout, TextKit uses these elements to lay out and render the text in your view.

The standard system views use an [`NSTextContentStorage`](nstextcontentstorage.md) object to manage their text content. When building a custom text view, use this type to store the text for your view. [`NSTextContentStorage`](nstextcontentstorage.md) works with an associated [`NSTextLayoutManager`](nstextlayoutmanager.md) to lay out your view’s text. When someone inserts new text or edits the existing text, call the [`performEditingTransaction(_:)`](nstextcontentmanager/performeditingtransaction(_:).md) method and use a block to modify the contents of the [`attributedString`](nstextcontentstorage/attributedstring.md) property. Wrapping your edits in an edit transaction lets the rest of the text system respond to those changes.

TextKit uses the abstract [`NSTextLocation`](nstextlocation.md) protocol to identify locations within text. [`NSTextContentStorage`](nstextcontentstorage.md) manager provides its own implementation of this protocol to represent locations within its storage object. To get the start and end locations, access the object’s [`documentRange`](nstextelementprovider/documentrange.md) property and use them to create new location objects. If you provide your own implementation of the [`NSTextLocation`](nstextlocation.md) protocol to manage locations in your content, subclass [`NSTextContentManager`](nstextcontentmanager.md) and implement your own storage object to support those locations.

## Topics

### Managing the stored text
- [var attributedString: NSAttributedString?](nstextcontentstorage/attributedstring.md)
  An attributed string that contains the contents of the document.
### Accessing paragraphs
- [var delegate: (any NSTextContentStorageDelegate)?](nstextcontentstorage/delegate.md)
  The delegate for the content storage object.
- [protocol NSTextContentStorageDelegate](nstextcontentstoragedelegate.md)
  The optional methods that delegates of content storage objects implement to handle content processing.
### Finding ranges, locations, and offsets
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextcontentstorage/location(_:offsetby:).md)
  Returns a new text location object based on an existing location and offset you provide.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextcontentstorage/offset(from:to:).md)
  Returns the number of characters between the specified locations.
- [func adjustedRange(from: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?](nstextcontentstorage/adjustedrange(from:foreditingtextselection:).md)
  Returns the text range, if any, in the backing store that required manual adjustment after editing.
### Managing text elements
- [func textElement(for: NSAttributedString) -> NSTextElement?](nstextcontentstorage/textelement(for:).md)
  Returns the text element corresponding to object’s attributed string.
- [func attributedString(for: NSTextElement) -> NSAttributedString?](nstextcontentstorage/attributedstring(for:).md)
  Returns a new attributed string for the text element.

## Relationships

### Inherits From
- [NSTextContentManager](nstextcontentmanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTextElementProvider](nstextelementprovider.md)
- [NSTextStorageObserving](nstextstorageobserving.md)

## See Also

- [class NSTextContentManager](nstextcontentmanager.md)
  An abstract class that defines the interface and a default implementation for managing the text document contents.
- [class NSAttributedString](../Foundation/NSAttributedString.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](../Foundation/NSMutableAttributedString.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage)*