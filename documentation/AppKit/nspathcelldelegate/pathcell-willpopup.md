# pathCell(_:willPopUp:)

**Framework**: AppKit  
**Kind**: method

Implement this method to customize the menu of a pop-up–style path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathCell(_ pathCell: NSPathCell, willPopUp menu: NSMenu)
```

#### Discussion

This method is called before the pop-up menu is shown. At this time, you can further customize the menu as required, adding and removing items. This method is called only when the style is set to `NSPathStylePopUp`.

Implementation of this method is optional.

## Parameters

- `pathCell`: The path cell that sent the message.
- `menu`: The pop-up menu to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcelldelegate/pathcell(_:willpopup:))*