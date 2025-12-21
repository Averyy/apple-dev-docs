# NSButton.ButtonType.multiLevelAccelerator

**Framework**: AppKit  
**Kind**: case

A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
case multiLevelAccelerator
```

#### Discussion

Use [`maxAcceleratorLevel`](nsbutton/maxacceleratorlevel.md) to configure the number of pressure levels. For other types of buttons, this property value defaults to `1`. For multilevel accelerator buttons, this property value defaults to `2`, and you can set it to a value between `1` and `5`.

Like a normal accelerator button, the button sends an action when the user first clicks it. If [`isContinuous`](nscontrol/iscontinuous.md) is [`true`](https://developer.apple.com/documentation/Swift/true), while the user clicks the button, it then sends actions at repeating intervals that are based on pressure. If [`isContinuous`](nscontrol/iscontinuous.md) is [`false`](https://developer.apple.com/documentation/Swift/false), the button sends actions as the user presses harder and reaches different levels of pressure. The button sends a final action when the user releases the button.

The value of a multilevel accelerator button is distinct from its state. The [`integerValue`](nscontrol/integervalue.md) of a multilevel button is `0` when the user doesn’t click it or `1` through `5` when the user clicks it, depending on the level of pressure. If you set the value of a multilevel accelerator button explicitly, the button doesn’t send an action until pressure reaches the level you specify.

On a system that doesn’t support pressure sensitivity, a multilevel accelerator button’s value is always `1` when the user clicks it.

This option corresponds to the Multi Level Accelerator type in Interface Builder’s Attributes inspector.

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
- [NSButton.ButtonType.switch](nsbutton/buttontype/switch.md)
  A standard checkbox button.
- [NSButton.ButtonType.radio](nsbutton/buttontype/radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](nsbutton/buttontype/accelerator.md)
  A button that sends repeating actions as pressure changes occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/multilevelaccelerator)*