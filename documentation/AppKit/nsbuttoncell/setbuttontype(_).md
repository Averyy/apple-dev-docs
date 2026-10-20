# setButtonType(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets how the button highlights while pressed and how it shows its state.

**Availability**:
- macOS

## Declaration

```swift
func setButtonType(_ type: NSButton.ButtonType)
```

```objc
- (void) setButtonType:(NSButtonType) type;
```

#### Discussion

The  [`setButtonType(_:)`](./setbuttontype%28_%29.md) method redisplays the button before returning.

The types available are for the most common button types, which are also accessible in Interface Builder; you can configure different behavior with the [`highlightsBy`](./highlightsby.md) and [`showsStateBy`](./showsstateby.md) properties.

Note that there is no `-buttonType` method. The set method sets various button properties that together establish the behavior of the type.

## Parameters

- `type`: A constant specifying the type of button. This can be one of the constants defined in [`NSButton.ButtonType`](../nsbutton/buttontype.md).

## See Also

### Related Documentation
- [var image: NSImage?](../nscell/image.md)
  The image displayed by the cell, if any.
- [var alternateImage: NSImage?](./alternateimage.md)
  The image the button displays in its alternate state.
### Displaying the Cell
- [var highlightsBy: NSCell.StyleMask](./highlightsby.md)
  A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).
- [var showsStateBy: NSCell.StyleMask](./showsstateby.md)
  The flags that indicate how the button cell shows its alternate state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setbuttontype(_:))*