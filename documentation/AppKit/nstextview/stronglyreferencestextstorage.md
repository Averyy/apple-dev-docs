# stronglyReferencesTextStorage

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether instances of the class operate in the object ownership policy.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class var stronglyReferencesTextStorage: Bool { get }
```

```objc
@property (class, readonly) BOOL stronglyReferencesTextStorage;
```

## Discussion

The default value is [`true`](../../Swift/true.md).

Under the policy, each text view strongly retains its text storage and its text container weakly references the view. In addition, the text views are compatible with `__weak storage`.

## See Also

### Accessing text system objects
- [class func fieldEditor() -> Self](./fieldeditor%28%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/stronglyreferencestextstorage)*