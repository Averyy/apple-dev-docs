# NSButton.ButtonType.pushOnPushOff

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A button that switches between on and off states with each click.

**Availability**:
- macOS

## Declaration

```swift
case pushOnPushOff
```

```c
NSButtonTypePushOnPushOff
```

## Discussion

When [`state`](../state.md) is [`on`](../../nscontrol/statevalue/on.md), the button appears illuminated. If the button has borders, it may also appear recessed. A second click returns the button’s [`state`](../state.md) to [`off`](../../nscontrol/statevalue/off.md).

This option corresponds to the Push On Push Off type in Interface Builder’s Attributes Inspector.

## See Also

### Configuring Button Behavior
- [NSButton.ButtonType.momentaryPushIn](./momentarypushin.md)
  A button that illuminates when the user clicks it.
- [NSButton.ButtonType.momentaryLight](./momentarylight.md)
  A button that displays a highlight when the user clicks it and returns to its normal state when the user releases it.
- [NSButton.ButtonType.momentaryChange](./momentarychange.md)
  A button that displays its alternate content when clicked and returns to its normal content when the user releases it.
- [NSButton.ButtonType.onOff](./onoff.md)
  A button that switches between a normal and emphasized bezel on each click.
- [NSButton.ButtonType.toggle](./toggle.md)
  A button that switches between its normal and alternate content on each click.
- [NSButton.ButtonType.switch](./switch.md)
  A standard checkbox button.
- [NSButton.ButtonType.radio](./radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](./accelerator.md)
  A button that sends repeating actions as pressure changes occur.
- [NSButton.ButtonType.multiLevelAccelerator](./multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/pushonpushoff)*