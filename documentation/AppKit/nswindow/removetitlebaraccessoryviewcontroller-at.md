# removeTitlebarAccessoryViewController(at:)

**Framework**: AppKit  
**Kind**: method

Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeTitlebarAccessoryViewController(at index: Int)
```

#### Discussion

You can also use [`removeFromParent()`](nsviewcontroller/removefromparent().md) to remove a specific title bar accessory view controller.

## Parameters

- `index`: The index in the array of title bar view controllers from which to remove the view controller.

## See Also

- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](nswindow/addtitlebaraccessoryviewcontroller(_:).md)
  Adds the specified title bar accessory view controller to the window.
- [func insertTitlebarAccessoryViewController(NSTitlebarAccessoryViewController, at: Int)](nswindow/inserttitlebaraccessoryviewcontroller(_:at:).md)
  Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.
- [var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController]](nswindow/titlebaraccessoryviewcontrollers.md)
  An array of title bar accessory view controllers that are currently added to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/removetitlebaraccessoryviewcontroller(at:))*