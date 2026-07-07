# inputPickerInteractionDidEndPresenting(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that the input picker view has finished presenting devices

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
optional func inputPickerInteractionDidEndPresenting(_ inputPickerInteraction: AVInputPickerInteraction)
```

#### Discussion

The `isPresented` property is set to `YES` at this point, indicating that the presentation is complete.

## Parameters

- `inputPickerInteraction`: The current AVInputPickerInteraction.

## See Also

- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbeginpresenting(_:).md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionWillBeginDismissing(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:).md)
  Tells the delegate that the input picker view is about to dismiss devices.
- [func inputPickerInteractionDidEndDismissing(AVInputPickerInteraction)](avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing(_:).md)
  Tells the delegate that the input picker view has finished dismissing devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidendpresenting(_:))*