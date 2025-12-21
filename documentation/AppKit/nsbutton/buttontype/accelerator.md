# NSButton.ButtonType.accelerator

**Framework**: AppKit  
**Kind**: case

A button that sends repeating actions as pressure changes occur.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
case accelerator
```

#### Discussion

A media player app, for example, might implement an accelerator button to allow a user to adjust the speed of fast forward or rewind with variable pressure. In this case, the button sends actions to the app to indicate when pressure on the button changes. The app then determines the amount of current pressure, and adjusts the playback speed accordingly.

An accelerator button sends an action when the user first clicks the button and continues sending actions until the user releases pressure on the button.

For accelerator buttons with [`isContinuous`](nscontrol/iscontinuous.md) set to [`true`](https://developer.apple.com/documentation/Swift/true), the interval between repeating actions automatically adjusts to match the pressure the user applies. Use [`setPeriodicDelay(_:interval:)`](nsbutton/setperiodicdelay(_:interval:).md) to configure the interval. As the user presses harder, the button sends actions more rapidly. As the user reduces pressure on the button, actions slow down. As such, the user has direct control over how fast the button sends actions. Typically, you use continuous accelerator buttons for continuously advancing through a series of discrete objects, such as photos in an album or pages in a book.

Noncontinuous accelerator buttons send actions whenever a change in force occurs. Typically, you use noncontinuous accelerator buttons to adjust the speed of navigation based on pressure, such as playback speed in a media player. After the user releases the button, the button sends a final action.

For buttons that aren’t accelerator buttons, the value of the button matches its state. For accelerator buttons, the value of the button is distinct from its state and indicates pressure level. When the user force clicks the button, [`doubleValue`](nscontrol/doublevalue.md) is a measurement of pressure between `1.0` and approaching `2.0`. When the user releases the button, `doubleValue` is `0.0`.

An accelerator button appears like any other button and doesn’t provide any visual indication that it supports variable pressure. To provide this type of visual indication, you can apply a custom [`image`](nsbutton/image.md) to the button.

On a system that doesn’t support pressure sensitivity, an accelerator button behaves like a button of type [`NSMomentaryLightButton`](nsmomentarylightbutton.md).

This option corresponds to the Accelerator type in Interface Builder’s Attributes inspector.

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
- [NSButton.ButtonType.multiLevelAccelerator](nsbutton/buttontype/multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/accelerator)*