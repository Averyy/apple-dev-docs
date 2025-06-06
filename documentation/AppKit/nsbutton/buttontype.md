# NSButton.ButtonType

**Framework**: AppKit  
**Kind**: enum

Button types that you can specify using [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
enum ButtonType
```

#### Overview

For examples of how these types behave, see [`Button Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Button.html#//apple_ref/doc/uid/10000019i).

## Topics

### Configuring Button Behavior
- [NSButton.ButtonType.momentaryPushIn](nsbutton/buttontype/momentarypushin.md)
  A button that illuminates when the user clicks it.
- [NSButton.ButtonType.momentaryLight](nsbutton/buttontype/momentarylight.md)
  A button that displays a highlight when the user clicks it and returns to its normal state when the user releases it.
- [NSButton.ButtonType.momentaryChange](nsbutton/buttontype/momentarychange.md)
  A button that displays its alternate content when clicked and returns to its normal content when the user releases it.
- [NSButton.ButtonType.pushOnPushOff](nsbutton/buttontype/pushonpushoff.md)
  A button that switches between on and off states with each click.
- [NSButton.ButtonType.onOff](nsbutton/buttontype/onoff.md)
  A button that switches between a normal and emphasized bezel on each click.
- [NSButton.ButtonType.toggle](nsbutton/buttontype/toggle.md)
  A button that switches between its normal and alternate content on each click.
- [NSButton.ButtonType.switch](nsbutton/buttontype/switch.md)
  A standard checkbox button.
- [NSButton.ButtonType.radio](nsbutton/buttontype/radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](nsbutton/buttontype/accelerator.md)
  A button that sends repeating actions as pressure changes occur.
- [NSButton.ButtonType.multiLevelAccelerator](nsbutton/buttontype/multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.
### Initializers
- [init?(rawValue: UInt)](nsbutton/buttontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum.md)
  The set of bezel styles to style buttons in your app.
- [NSButton.GradientType](nsbutton/gradienttype.md)
  Specify the gradients used by the [`gradientType`](nsbuttoncell/gradienttype.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype)*