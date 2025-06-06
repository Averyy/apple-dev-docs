# insertTitlebarAccessoryViewController(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func insertTitlebarAccessoryViewController(_ childViewController: NSTitlebarAccessoryViewController, at index: Int)
```

## Parameters

- `childViewController`: The title bar accessory view controller to insert.
- `index`: The index at which to insert  .

## See Also

- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](nswindow/addtitlebaraccessoryviewcontroller(_:).md)
  Adds the specified title bar accessory view controller to the window.
- [func removeTitlebarAccessoryViewController(at: Int)](nswindow/removetitlebaraccessoryviewcontroller(at:).md)
  Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.
- [var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController]](nswindow/titlebaraccessoryviewcontrollers.md)
  An array of title bar accessory view controllers that are currently added to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/inserttitlebaraccessoryviewcontroller(_:at:))*