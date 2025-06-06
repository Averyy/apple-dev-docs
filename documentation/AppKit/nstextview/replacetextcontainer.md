# replaceTextContainer(_:)

**Framework**: AppKit  
**Kind**: method

Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func replaceTextContainer(_ newContainer: NSTextContainer)
```

## Parameters

- `newContainer`: The new text container. This method raises   if   is  .

## See Also

- [init(frame: NSRect, textContainer: NSTextContainer?)](nstextview/init(frame:textcontainer:).md)
  Initializes a text view.
- [class var stronglyReferencesTextStorage: Bool](nstextview/stronglyreferencestextstorage.md)
- [class func fieldEditor() -> Self](nstextview/fieldeditor.md)
- [var textContainer: NSTextContainer?](nstextview/textcontainer.md)
  The receiver’s text container.
- [var textContainerInset: NSSize](nstextview/textcontainerinset.md)
  The empty space the receiver leaves around its associated text container.
- [var textContainerOrigin: NSPoint](nstextview/textcontainerorigin.md)
  The origin of the receiver’s text container.
- [func invalidateTextContainerOrigin()](nstextview/invalidatetextcontainerorigin.md)
  Invalidates the calculated origin of the text container.
- [var textLayoutManager: NSTextLayoutManager?](nstextview/textlayoutmanager.md)
  The manager that lays out text for the receiver’s text container.
- [var layoutManager: NSLayoutManager?](nstextview/layoutmanager.md)
  The layout manager that lays out text for the receiver’s text container.
- [var textContentStorage: NSTextContentStorage?](nstextview/textcontentstorage.md)
  The receiver’s text storage object.
- [var textStorage: NSTextStorage?](nstextview/textstorage.md)
  The receiver’s text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/replacetextcontainer(_:))*