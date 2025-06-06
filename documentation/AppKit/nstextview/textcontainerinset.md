# textContainerInset

**Framework**: AppKit  
**Kind**: property

The empty space the receiver leaves around its associated text container.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var textContainerInset: NSSize { get set }
```

#### Discussion

It is possible to set the text container and view sizes and resizing behavior so that the inset cannot be maintained exactly, although the text system tries to maintain the inset wherever possible. In any case, the [`textContainerOrigin`](nstextview/textcontainerorigin.md) and size of the text container are authoritative as to the location of the text container within the view.

The text itself can have an additional inset, inside the text container, specified by the [`lineFragmentPadding`](nstextcontainer/linefragmentpadding.md) method of `NSTextContainer`.

## See Also

- [class var stronglyReferencesTextStorage: Bool](nstextview/stronglyreferencestextstorage.md)
- [class func fieldEditor() -> Self](nstextview/fieldeditor.md)
- [var textContainer: NSTextContainer?](nstextview/textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](nstextview/replacetextcontainer(_:).md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/textcontainerinset)*