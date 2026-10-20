# replaceTextContainer(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.

**Availability**:
- macOS

## Declaration

```swift
func replaceTextContainer(_ newContainer: NSTextContainer)
```

```objc
- (void) replaceTextContainer:(NSTextContainer *) newContainer;
```

## Parameters

- `newContainer`: The new text container. This method raises `NSInvalidArgumentException` if `aTextContainer` is `nil`.

## See Also

### Related Documentation
- [init(frame: NSRect, textContainer: NSTextContainer?)](./init%28frame,textcontainer%29.md)
  Initializes a text view.
### Accessing text system objects
- [class var stronglyReferencesTextStorage: Bool](./stronglyreferencestextstorage.md)
  A Boolean value that indicates whether instances of the class operate in the object ownership policy.
- [class func fieldEditor() -> Self](./fieldeditor%28%29.md)
- [var textContainer: NSTextContainer?](./textcontainer.md)
  The receiver’s text container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/replacetextcontainer(_:))*