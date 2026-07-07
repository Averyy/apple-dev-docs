# inputPickerInteractionDidEndDismissing(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that the input picker view has finished dismissing devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
optional func inputPickerInteractionDidEndDismissing(_ inputPickerInteraction: AVInputPickerInteraction)
```

#### Discussion

The `isPresented` property is set to `NO` at this point, indicating that the dismissal is complete.

## Parameters

- `inputPickerInteraction`: The current AVInputPickerInteraction.

## See Also

- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbeginpresenting(_:).md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionDidEndPresenting(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidendpresenting(_:).md)
  Tells the delegate that the input picker view has finished presenting devices
- [func inputPickerInteractionWillBeginDismissing(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:).md)
  Tells the delegate that the input picker view is about to dismiss devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing(_:))*