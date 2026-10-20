# invalidateTextContainerOrigin()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the calculated origin of the text container.

**Availability**:
- macOS

## Declaration

```swift
func invalidateTextContainerOrigin()
```

```objc
- (void) invalidateTextContainerOrigin;
```

#### Discussion

This method is invoked automatically; you should never need to invoke it directly. Usually called because the text view has been resized or the contents of the text container have changed.

## See Also

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
- [var textContainerOrigin: NSPoint](./textcontainerorigin.md)
  The origin of the receiver’s text container.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The manager that lays out text for the receiver’s text container.
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The layout manager that lays out text for the receiver’s text container.
- [var textContentStorage: NSTextContentStorage?](./textcontentstorage.md)
  The receiver’s text storage object.
- [var textStorage: NSTextStorage?](./textstorage.md)
  The receiver’s text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/invalidatetextcontainerorigin())*