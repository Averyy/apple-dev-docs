# AVInputPickerInteraction.Delegate

**Framework**: AVKit  
**Kind**: protocol

The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

## Topics

### Responding to life cycle events
- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbeginpresenting(_:).md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionDidEndPresenting(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidendpresenting(_:).md)
  Tells the delegate that the input picker view has finished presenting devices
- [func inputPickerInteractionWillBeginDismissing(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:).md)
  Tells the delegate that the input picker view is about to dismiss devices.
- [func inputPickerInteractionDidEndDismissing(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing(_:).md)
  Tells the delegate that the input picker view has finished dismissing devices.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVInputPickerInteraction.Delegate)?](avinputpickerinteraction/delegate-swift.property.md)
  The input picker view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol)*