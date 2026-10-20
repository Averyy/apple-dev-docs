# contents

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

An array of objects to display in the list view.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var contents: [Any] { get set }
```

```objc
@property (copy) NSArray<id> * contents;
```

#### Discussion

The list view controller asks its delegate for a new content view controller for each object in `contents`, and sets the [`representedObject`](../../AppKit/nsviewcontroller/representedobject.md) of the newly created content view controller accordingly. To optimize content resetting, the list view controller may reuse content view controllers for identical objects that already exist in `contents`.

## See Also

### Accessing Content
- [func row(for: NSViewController) -> Int](./row%28for%29.md)
  Returns the row represented by the specified content view controller.
- [func viewController(atRow: Int, makeIfNecessary: Bool) -> NSViewController](./viewcontroller%28atrow,makeifnecessary%29.md)
  Returns the content view controller associated with the specified row, or a new content view controller if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/contents)*