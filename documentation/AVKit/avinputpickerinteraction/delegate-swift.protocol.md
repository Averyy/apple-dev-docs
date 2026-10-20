# AVInputPickerInteraction.Delegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol AVInputPickerInteractionDelegate <NSObject>
```

## Topics

### Responding to life cycle events
- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](./delegate-swift.protocol/inputpickerinteractionwillbeginpresenting%28_%29.md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionDidEndPresenting(AVInputPickerInteraction)](./delegate-swift.protocol/inputpickerinteractiondidendpresenting%28_%29.md)
  Tells the delegate that the input picker view has finished presenting devices
- [func inputPickerInteractionWillBeginDismissing(AVInputPickerInteraction)](./delegate-swift.protocol/inputpickerinteractionwillbegindismissing%28_%29.md)
  Tells the delegate that the input picker view is about to dismiss devices.
- [func inputPickerInteractionDidEndDismissing(AVInputPickerInteraction)](./delegate-swift.protocol/inputpickerinteractiondidenddismissing%28_%29.md)
  Tells the delegate that the input picker view has finished dismissing devices.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the delegate
- [var delegate: (any AVInputPickerInteraction.Delegate)?](./delegate-swift.property.md)
  The input picker view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol)*