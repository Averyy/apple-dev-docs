# pathCell(_:willDisplay:)

**Framework**: AppKit  
**Kind**: method

Implement this method to customize the Open panel shown by a pop-up–style path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathCell(_ pathCell: NSPathCell, willDisplay openPanel: NSOpenPanel)
```

#### Discussion

This method is called before the Open panel is shown but after its allowed file types are set to the cell’s allowed types. At this time, you can further customize the Open panel as required. This method is called only when the style is set to `NSPathStylePopUp`.

Implementation of this method is optional.

## Parameters

- `pathCell`: The path cell that sent the message.
- `openPanel`: The Open panel to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcelldelegate/pathcell(_:willdisplay:))*