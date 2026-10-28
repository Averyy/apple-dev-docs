# NSButton.ButtonType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Button types that you can specify using [`setButtonType(_:)`](../nsbuttoncell/setbuttontype%28_%29.md).

**Availability**:
- macOS

## Declaration

```swift
enum ButtonType
```

```c
enum NSButtonType : NSUInteger;
```

## Overview

For more information, see [`setButtonType(_:)`](../nsbuttoncell/setbuttontype%28_%29.md).

## Topics

### Configuring Button Behavior
- [NSButton.ButtonType.momentaryPushIn](./buttontype/momentarypushin.md)
  A button that illuminates when the user clicks it.
- [NSButton.ButtonType.momentaryLight](./buttontype/momentarylight.md)
  A button that displays a highlight when the user clicks it and returns to its normal state when the user releases it.
- [NSButton.ButtonType.momentaryChange](./buttontype/momentarychange.md)
  A button that displays its alternate content when clicked and returns to its normal content when the user releases it.
- [NSButton.ButtonType.pushOnPushOff](./buttontype/pushonpushoff.md)
  A button that switches between on and off states with each click.
- [NSButton.ButtonType.onOff](./buttontype/onoff.md)
  A button that switches between a normal and emphasized bezel on each click.
- [NSButton.ButtonType.toggle](./buttontype/toggle.md)
  A button that switches between its normal and alternate content on each click.
- [NSButton.ButtonType.switch](./buttontype/switch.md)
  A standard checkbox button.
- [NSButton.ButtonType.radio](./buttontype/radio.md)
  A button that displays a single selected value from group of possible choices.
- [NSButton.ButtonType.accelerator](./buttontype/accelerator.md)
  A button that sends repeating actions as pressure changes occur.
- [NSButton.ButtonType.multiLevelAccelerator](./buttontype/multilevelaccelerator.md)
  A button that allows for a configurable number of stepped pressure levels and provides tactile feedback as the user reaches each step.
### Deprecated
- [Deprecated symbols](../buttontype-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Initializers
- [init?(rawValue: UInt)](./buttontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSButton.BezelStyle](./bezelstyle-swift.enum.md)
  The set of bezel styles to style buttons in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/buttontype)*