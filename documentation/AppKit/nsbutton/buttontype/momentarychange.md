# NSButton.ButtonType.momentaryChange

**Framework**: AppKit  
**Kind**: case

A button that displays its alternate content when clicked and returns to its normal content when the user releases it.

**Availability**:
- macOS ?+

## Declaration

```swift
case momentaryChange
```

#### Discussion

When the value of [`isHighlighted`](nscontrol/ishighlighted.md) is [`true`](https://developer.apple.com/documentation/swift/true), the button displays its alternate content (for example, its [`alternateImage`](nsbutton/alternateimage.md) or [`alternateTitle`](nsbutton/alternatetitle.md)). If the button has no alternate content to display, it may instead draw its normal content using an illuminated effect. When [`isHighlighted`](nscontrol/ishighlighted.md) is [`false`](https://developer.apple.com/documentation/swift/false), the button displays its normal content (for example, its [`image`](nsbutton/image.md) or [`title`](nsbutton/title.md)).

This option corresponds to the Momentary Change type in Interface Builder’s Attributes inspector.

## See Also

- [NSButton.ButtonType.momentaryPushIn](nsbutton/buttontype/momentarypushin.md)
  A button that illuminates when the user clicks it.
- [NSButton.ButtonType.momentaryLight](nsbutton/buttontype/momentarylight.md)
  A button that displays a highlight when the user clicks it and returns to its normal state when the user releases it.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/momentarychange)*