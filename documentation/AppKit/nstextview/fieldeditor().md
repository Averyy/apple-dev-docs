# fieldEditor()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 10.14+

## Declaration

```swift
class func fieldEditor() -> Self
```

```objc
+ (instancetype) fieldEditor;
```

## See Also

### Accessing text system objects
- [class var stronglyReferencesTextStorage: Bool](./stronglyreferencestextstorage.md)
  A Boolean value that indicates whether instances of the class operate in the object ownership policy.
- [var textContainer: NSTextContainer?](./textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](./replacetextcontainer%28_%29.md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
- [var textContainerInset: NSSize](./textcontainerinset.md)
  The empty space the receiver leaves around its associated text container.
- [var textContainerOrigin: NSPoint](./textcontainerorigin.md)
  The origin of the receiver’s text container.
- [func invalidateTextContainerOrigin()](./invalidatetextcontainerorigin%28%29.md)
  Invalidates the calculated origin of the text container.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The manager that lays out text for the receiver’s text container.
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The layout manager that lays out text for the receiver’s text container.
- [var textContentStorage: NSTextContentStorage?](./textcontentstorage.md)
  The receiver’s text storage object.
- [var textStorage: NSTextStorage?](./textstorage.md)
  The receiver’s text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/fieldeditor())*