# setButtonType(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the button’s type, which affects its user interface and behavior when clicked.

**Availability**:
- macOS

## Declaration

```swift
func setButtonType(_ type: NSButton.ButtonType)
```

```objc
- (void) setButtonType:(NSButtonType) type;
```

## Discussion

This method causes the button to update to reflect the new type before the method finishes executing.

The types available are for the most common button types, which are also accessible in Interface Builder. You can configure different behavior with the `NSButtonCell` methods  [`highlightsBy`](../nsbuttoncell/highlightsby.md) and [`showsStateBy`](../nsbuttoncell/showsstateby.md).

Note that there is no `-buttonType` method. The set method sets various button properties that together establish the behavior of the type.

## Parameters

- `type`: A constant specifying the type of the button. The available button types are listed under [`NSButton.ButtonType`](./buttontype.md) in the [`NSButtonCell`](../nsbuttoncell.md) class.

## See Also

### Related Documentation
- [var image: NSImage?](./image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [func setButtonType(NSButton.ButtonType)](../nsbuttoncell/setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
- [var alternateImage: NSImage?](./alternateimage.md)
  An alternate image that appears on the button when the button is in an on state.
### Configuring buttons
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns by reference the delay and interval periods for a continuous button.
- [func setPeriodicDelay(Float, interval: Float)](./setperiodicdelay%28_,interval%29.md)
  Sets the message delay and interval periods for a continuous button.
- [var contentTintColor: NSColor?](./contenttintcolor.md)
  A tint color to use for the template image and text content.
- [var hasDestructiveAction: Bool](./hasdestructiveaction.md)
  A Boolean value that defines whether a button’s action has a destructive effect.
- [var alternateTitle: String](./alternatetitle.md)
  The title that the button displays when the button is in an on state.
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title that the button displays in an off state, as an attributed string.
- [var attributedAlternateTitle: NSAttributedString](./attributedalternatetitle.md)
  The title that the button displays as an attributed string when the button is in an on state.
- [var title: String](./title.md)
  The title displayed on the button when it’s in an off state.
- [var symbolConfiguration: NSImage.SymbolConfiguration?](./symbolconfiguration.md)
  The combination of point size, weight, and scale to use when sizing and displaying symbol images.
- [var sound: NSSound?](./sound.md)
  The sound that plays when the user clicks the button.
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the button.
- [var maxAcceleratorLevel: Int](./maxacceleratorlevel.md)
  An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](../nsmultilevelacceleratorbutton.md).
- [var tintProminence: NSTintProminence](./tintprominence.md)
  The tint prominence of the button. Use tint prominence to gently suggest a hierarchy when multiple buttons perform similar actions. A button with primary tint prominence suggests the most preferred option, while secondary prominence indicates a reasonable alternative. See [`NSTintProminence`](../nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](../nstintprominence.md)
  Controls how strongly the tint color applies in a view.
- [var borderShape: NSControl.BorderShape](./bordershape.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/setbuttontype(_:))*