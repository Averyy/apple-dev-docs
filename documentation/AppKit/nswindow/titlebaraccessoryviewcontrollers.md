# titlebarAccessoryViewControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of title bar accessory view controllers that are currently added to the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController] { get set }
```

```objc
@property (copy) NSArray<__kindof NSTitlebarAccessoryViewController *> * titlebarAccessoryViewControllers;
```

## See Also

### Managing Title Bar Accessories
- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](./addtitlebaraccessoryviewcontroller%28_%29.md)
  Adds the specified title bar accessory view controller to the window.
- [func insertTitlebarAccessoryViewController(NSTitlebarAccessoryViewController, at: Int)](./inserttitlebaraccessoryviewcontroller%28_,at%29.md)
  Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.
- [func removeTitlebarAccessoryViewController(at: Int)](./removetitlebaraccessoryviewcontroller%28at%29.md)
  Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlebaraccessoryviewcontrollers)*