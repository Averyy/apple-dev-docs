# inputPickerInteractionWillBeginDismissing(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the input picker view is about to dismiss devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func inputPickerInteractionWillBeginDismissing(_ inputPickerInteraction: AVInputPickerInteraction)
```

```objc
- (void) inputPickerInteractionWillBeginDismissing:(AVInputPickerInteraction *) inputPickerInteraction;
```

## Parameters

- `inputPickerInteraction`: The current AVInputPickerInteraction.

## See Also

### Responding to life cycle events
- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](./inputpickerinteractionwillbeginpresenting%28_%29.md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionDidEndPresenting(AVInputPickerInteraction)](./inputpickerinteractiondidendpresenting%28_%29.md)
  Tells the delegate that the input picker view has finished presenting devices
- [func inputPickerInteractionDidEndDismissing(AVInputPickerInteraction)](./inputpickerinteractiondidenddismissing%28_%29.md)
  Tells the delegate that the input picker view has finished dismissing devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:))*