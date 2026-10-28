# textContainerOrigin

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The origin of the receiver’s text container.

**Availability**:
- macOS

## Declaration

```swift
var textContainerOrigin: NSPoint { get }
```

```objc
@property (readonly) NSPoint textContainerOrigin;
```

## Discussion

Calculated from the receiver’s bounds rectangle, container inset, and the container’s used rect.

## See Also

### Related Documentation
- [func usedRect(for: NSTextContainer) -> NSRect](../nslayoutmanager/usedrect%28for%29.md)
  Returns the bounding rectangle for the glyphs in the specified text container.
### Accessing text system objects
- [class var stronglyReferencesTextStorage: Bool](./stronglyreferencestextstorage.md)
  A Boolean value that indicates whether instances of the class operate in the object ownership policy.
- [class func fieldEditor() -> Self](./fieldeditor%28%29.md)
- [var textContainer: NSTextContainer?](./textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](./replacetextcontainer%28_%29.md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
- [var textContainerInset: NSSize](./textcontainerinset.md)
  The empty space the receiver leaves around its associated text container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/textcontainerorigin)*