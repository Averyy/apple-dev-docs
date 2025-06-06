# contents

**Framework**: Notification Center  
**Kind**: property

An array of objects to display in the list view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var contents: [Any] { get set }
```

#### Discussion

The list view controller asks its delegate for a new content view controller for each object in `contents`, and sets the [`representedObject`](https://developer.apple.com/documentation/AppKit/NSViewController/representedObject) of the newly created content view controller accordingly. To optimize content resetting, the list view controller may reuse content view controllers for identical objects that already exist in `contents`.

## See Also

- [func row(for: NSViewController) -> Int](ncwidgetlistviewcontroller/row(for:).md)
  Returns the row represented by the specified content view controller.
- [func viewController(atRow: Int, makeIfNecessary: Bool) -> NSViewController](ncwidgetlistviewcontroller/viewcontroller(atrow:makeifnecessary:).md)
  Returns the content view controller associated with the specified row, or a new content view controller if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/contents)*