# messageComposeViewController(_:didFinishWith:)

**Framework**: Message UI  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user finished composing the message.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult)
```

#### Discussion

This method is called when the user taps one of the buttons to dismiss the message composition interface. Your implementation of this method should dismiss the view controller and perform any additional actions needed to process the sending of the message. The result parameter lets you know whether the user chose to cancel or send the message, or whether sending the message failed.

Implementation of this method is required.

## Parameters

- `controller`: The message composition view controller that is returning the result.
- `result`: A result code that indicates how the user chose to complete the composition. See the   enumeration.

## See Also

- [enum MessageComposeResult](messagecomposeresult.md)
  These constants describe the result of the message-composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:))*