# userInterfaceLayoutDirection

**Framework**: AppKit  
**Kind**: property

Configures the layout direction of menu items in the menu.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }
```

#### Discussion

This property configures the layout direction (a value of type [`NSUserInterfaceLayoutDirection`](nsuserinterfacelayoutdirection.md)) of menu items in the menu. If no layout direction is explicitly set for a menu, then the menu defaults to the layout direction specified for the application object. See [`userInterfaceLayoutDirection`](nsapplication/userinterfacelayoutdirection.md) in [`NSApplication`](nsapplication.md).

## See Also

- [enum NSUserInterfaceLayoutDirection](nsuserinterfacelayoutdirection.md)
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/userinterfacelayoutdirection)*