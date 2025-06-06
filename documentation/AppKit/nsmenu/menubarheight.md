# menuBarHeight

**Framework**: AppKit  
**Kind**: property

The menu bar height for the main menu in pixels.

**Availability**:
- macOS ?+

## Declaration

```swift
var menuBarHeight: CGFloat { get }
```

#### Discussion

For the main menu, the value of this property is a value of type `CGFloat`, indicating the height of the menu bar in pixels. For any other menu, the value of this property is `0`.

This property supersedes the `menuBarHeight` class method of the `NSMenuView` class.

## See Also

- [class func menuBarVisible() -> Bool](nsmenu/menubarvisible.md)
  Returns a Boolean value that indicates whether the menu bar is visible.
- [class func setMenuBarVisible(Bool)](nsmenu/setmenubarvisible(_:).md)
  Sets whether the menu bar is visible and selectable by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menubarheight)*