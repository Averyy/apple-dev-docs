# inputPickerInteractionDidEndPresenting(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the input picker view has finished presenting devices

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func inputPickerInteractionDidEndPresenting(_ inputPickerInteraction: AVInputPickerInteraction)
```

```objc
- (void) inputPickerInteractionDidEndPresenting:(AVInputPickerInteraction *) inputPickerInteraction;
```

#### Discussion

The `isPresented` property is set to `YES` at this point, indicating that the presentation is complete.

## Parameters

- `inputPickerInteraction`: The current AVInputPickerInteraction.

## See Also

### Responding to life cycle events
- [func inputPickerInteractionWillBeginPresenting(AVInputPickerInteraction)](./inputpickerinteractionwillbeginpresenting%28_%29.md)
  Tells the delegate that the input picker view is about to present devices.
- [func inputPickerInteractionWillBeginDismissing(AVInputPickerInteraction)](./inputpickerinteractionwillbegindismissing%28_%29.md)
  Tells the delegate that the input picker view is about to dismiss devices.
- [func inputPickerInteractionDidEndDismissing(AVInputPickerInteraction)](./inputpickerinteractiondidenddismissing%28_%29.md)
  Tells the delegate that the input picker view has finished dismissing devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidendpresenting(_:))*