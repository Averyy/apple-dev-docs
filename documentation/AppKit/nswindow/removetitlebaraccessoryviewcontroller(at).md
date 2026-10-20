# removeTitlebarAccessoryViewController(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeTitlebarAccessoryViewController(at index: Int)
```

```objc
- (void) removeTitlebarAccessoryViewControllerAtIndex:(NSInteger) index;
```

#### Discussion

You can also use [`removeFromParent()`](../nsviewcontroller/removefromparent%28%29.md) to remove a specific title bar accessory view controller.

## Parameters

- `index`: The index in the array of title bar view controllers from which to remove the view controller.

## See Also

### Managing Title Bar Accessories
- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](./addtitlebaraccessoryviewcontroller%28_%29.md)
  Adds the specified title bar accessory view controller to the window.
- [func insertTitlebarAccessoryViewController(NSTitlebarAccessoryViewController, at: Int)](./inserttitlebaraccessoryviewcontroller%28_,at%29.md)
  Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.
- [var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController]](./titlebaraccessoryviewcontrollers.md)
  An array of title bar accessory view controllers that are currently added to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/removetitlebaraccessoryviewcontroller(at:))*