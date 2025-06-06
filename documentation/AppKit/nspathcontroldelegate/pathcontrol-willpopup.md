# pathControl(_:willPopUp:)

**Framework**: AppKit  
**Kind**: method

Implement this method to customize the menu of a pop-up–style path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, willPopUp menu: NSMenu)
```

#### Discussion

This method is called before the pop-up menu is shown. At this time, you can further customize the menu as required, adding and removing items. This method is called only when the style is set to `NSPathStylePopUp`. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control displaying the pop-up menu.
- `menu`: The pop-up menu to be displayed.

## See Also

- [func pathControl(NSPathControl, willDisplay: NSOpenPanel)](nspathcontroldelegate/pathcontrol(_:willdisplay:).md)
  Implement this method to customize the Open panel shown by a pop-up–style path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:willpopup:))*