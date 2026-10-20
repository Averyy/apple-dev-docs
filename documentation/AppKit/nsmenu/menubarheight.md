# menuBarHeight

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu bar height for the main menu in pixels.

**Availability**:
- macOS

## Declaration

```swift
var menuBarHeight: CGFloat { get }
```

```objc
@property (readonly) CGFloat menuBarHeight;
```

#### Discussion

For the main menu, the value of this property is a value of type `CGFloat`, indicating the height of the menu bar in pixels. For any other menu, the value of this property is `0`.

This property supersedes the `menuBarHeight` class method of the `NSMenuView` class.

## See Also

### Managing the Menu Bar
- [class func menuBarVisible() -> Bool](./menubarvisible%28%29.md)
  Returns a Boolean value that indicates whether the menu bar is visible.
- [class func setMenuBarVisible(Bool)](./setmenubarvisible%28_%29.md)
  Sets whether the menu bar is visible and selectable by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menubarheight)*