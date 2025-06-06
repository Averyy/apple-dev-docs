# insertNewButtonImage(_:in:)

**Framework**: AppKit  
**Kind**: method

Sets the image used for the specified button cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertNewButtonImage(_ newButtonImage: NSImage, in buttonCell: NSButtonCell)
```

#### Discussion

Called by the color panel to insert a new image into the specified cell by invoking `NSButtonCell`’s setImage: method. Override this method to customize `newButtonImage` before insertion in `buttonCell`.

## Parameters

- `newButtonImage`: The image used for the specified button cell.
- `buttonCell`: The button cell for which to set the image.

## See Also

- [var provideNewButtonImage: NSImage](nscolorpicker/providenewbuttonimage.md)
  The button image used by the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/insertnewbuttonimage(_:in:))*