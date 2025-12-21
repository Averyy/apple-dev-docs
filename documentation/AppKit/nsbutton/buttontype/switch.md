# NSButton.ButtonType.switch

**Framework**: AppKit  
**Kind**: case

A standard checkbox button.

**Availability**:
- macOS ?+

## Declaration

```swift
case `switch`
```

#### Discussion

A switch button provides the same toggling behavior as a [`NSButton.ButtonType.toggle`](nsbutton/buttontype/toggle.md) button. In addition to configuring that behavior, this button type configures [`isBordered`](nsbutton/isbordered.md) to [`false`](https://developer.apple.com/documentation/Swift/false) and provides a standard checkbox image.

Checkboxes are ideal for controlling a Boolean state within your application. The mixed state of a checkbox, enabled through the [`allowsMixedState`](nsbutton/allowsmixedstate.md) property, is useful for summarizing multiple Boolean states of varying values.

This option corresponds to the Switch type in Interface Builder’s Attributes inspector.

## See Also

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
- [NSButton.ButtonType.radio](nsbutton/buttontype/radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](nsbutton/buttontype/accelerator.md)
  A button that sends repeating actions as pressure changes occur.
- [NSButton.ButtonType.multiLevelAccelerator](nsbutton/buttontype/multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/switch)*