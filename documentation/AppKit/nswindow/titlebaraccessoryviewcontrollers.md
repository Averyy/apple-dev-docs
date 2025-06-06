# titlebarAccessoryViewControllers

**Framework**: AppKit  
**Kind**: property

An array of title bar accessory view controllers that are currently added to the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController] { get set }
```

## See Also

- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](nswindow/addtitlebaraccessoryviewcontroller(_:).md)
  Adds the specified title bar accessory view controller to the window.
- [func insertTitlebarAccessoryViewController(NSTitlebarAccessoryViewController, at: Int)](nswindow/inserttitlebaraccessoryviewcontroller(_:at:).md)
  Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.
- [func removeTitlebarAccessoryViewController(at: Int)](nswindow/removetitlebaraccessoryviewcontroller(at:).md)
  Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlebaraccessoryviewcontrollers)*