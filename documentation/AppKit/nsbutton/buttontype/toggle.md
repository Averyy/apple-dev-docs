# NSButton.ButtonType.toggle

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A button that switches between its normal and alternate content on each click.

**Availability**:
- macOS

## Declaration

```swift
case toggle
```

```c
NSButtonTypeToggle
```

#### Discussion

When the value of [`state`](../state.md) is [`off`](../../nscontrol/statevalue/off.md), the button displays its normal content, such as its [`image`](../image.md) or [`title`](../title.md). When [`state`](../state.md) has any other value, the button displays its alternate content, such as its [`alternateImage`](../../nsbuttoncell/alternateimage.md) or [`alternateTitle`](../alternatetitle.md) instead. If the button has no alternate content to display, it may instead draw its normal content using an illuminated effect.

This type of button is best for controlling a Boolean state within your application, while also providing a visual indication of that state.

This option corresponds to the Toggle type in Interface Builder’s Attributes Inspector.

## See Also

### Configuring Button Behavior
- [NSButton.ButtonType.momentaryPushIn](./momentarypushin.md)
  A button that illuminates when the user clicks it.
- [NSButton.ButtonType.momentaryLight](./momentarylight.md)
  A button that displays a highlight when the user clicks it and returns to its normal state when the user releases it.
- [NSButton.ButtonType.momentaryChange](./momentarychange.md)
  A button that displays its alternate content when clicked and returns to its normal content when the user releases it.
- [NSButton.ButtonType.pushOnPushOff](./pushonpushoff.md)
  A button that switches between on and off states with each click.
- [NSButton.ButtonType.onOff](./onoff.md)
  A button that switches between a normal and emphasized bezel on each click.
- [NSButton.ButtonType.switch](./switch.md)
  A standard checkbox button.
- [NSButton.ButtonType.radio](./radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](./accelerator.md)
  A button that sends repeating actions as pressure changes occur.
- [NSButton.ButtonType.multiLevelAccelerator](./multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle)*