# stronglyReferencesTextStorage

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether instances of the class operate in the object ownership policy.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class var stronglyReferencesTextStorage: Bool { get }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

Under the policy, each text view strongly retains its text storage and its text container weakly references the view. In addition, the text views are compatible with `__weak storage`.

## See Also

- [class func fieldEditor() -> Self](nstextview/fieldeditor.md)
- [var textContainer: NSTextContainer?](nstextview/textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](nstextview/replacetextcontainer(_:).md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/stronglyreferencestextstorage)*