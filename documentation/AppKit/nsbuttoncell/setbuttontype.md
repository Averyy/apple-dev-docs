# setButtonType(_:)

**Framework**: AppKit  
**Kind**: method

Sets how the button highlights while pressed and how it shows its state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setButtonType(_ type: NSButton.ButtonType)
```

#### Discussion

The  [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md) method redisplays the button before returning.

The types available are for the most common button types, which are also accessible in Interface Builder; you can configure different behavior with the [`highlightsBy`](nsbuttoncell/highlightsby.md) and [`showsStateBy`](nsbuttoncell/showsstateby.md) properties.

Note that there is no `-buttonType` method. The set method sets various button properties that together establish the behavior of the type.

## Parameters

- `type`: A constant specifying the type of button. This can be one of the constants defined in  .

## See Also

- [var image: NSImage?](nscell/image.md)
  The image displayed by the cell, if any.
- [var alternateImage: NSImage?](nsbuttoncell/alternateimage.md)
  The image the button displays in its alternate state.
- [var highlightsBy: NSCell.StyleMask](nsbuttoncell/highlightsby.md)
  A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).
- [var showsStateBy: NSCell.StyleMask](nsbuttoncell/showsstateby.md)
  The flags that indicate how the button cell shows its alternate state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setbuttontype(_:))*