# setMenuBarVisible(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sets whether the menu bar is visible and selectable by the user.

**Availability**:
- macOS

## Declaration

```swift
class func setMenuBarVisible(_ visible: Bool)
```

```objc
+ (void) setMenuBarVisible:(BOOL) visible;
```

## Parameters

- `visible`: [`true`](../../Swift/true.md) if the menu bar should be visible and selectable, otherwise [`false`](../../Swift/false.md).

## See Also

### Managing the Menu Bar
- [class func menuBarVisible() -> Bool](./menubarvisible%28%29.md)
  Returns a Boolean value that indicates whether the menu bar is visible.
- [var menuBarHeight: CGFloat](./menubarheight.md)
  The menu bar height for the main menu in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/setmenubarvisible(_:))*