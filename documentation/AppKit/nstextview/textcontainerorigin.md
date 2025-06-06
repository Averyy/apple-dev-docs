# textContainerOrigin

**Framework**: AppKit  
**Kind**: property

The origin of the receiver’s text container.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var textContainerOrigin: NSPoint { get }
```

#### Discussion

Calculated from the receiver’s bounds rectangle, container inset, and the container’s used rect.

## See Also

- [func usedRect(for: NSTextContainer) -> NSRect](nslayoutmanager/usedrect(for:).md)
  Returns the bounding rectangle for the glyphs in the specified text container.
- [class var stronglyReferencesTextStorage: Bool](nstextview/stronglyreferencestextstorage.md)
- [class func fieldEditor() -> Self](nstextview/fieldeditor.md)
- [var textContainer: NSTextContainer?](nstextview/textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](nstextview/replacetextcontainer(_:).md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
- [var textContainerInset: NSSize](nstextview/textcontainerinset.md)
  The empty space the receiver leaves around its associated text container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/textcontainerorigin)*