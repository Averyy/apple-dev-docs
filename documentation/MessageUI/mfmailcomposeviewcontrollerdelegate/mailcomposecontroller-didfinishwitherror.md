# mailComposeController(_:didFinishWith:error:)

**Framework**: Message UI  
**Kind**: method

Tells the delegate that the user wants to dismiss the mail composition view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: (any Error)?)
```

#### Discussion

Your implementation of this method should dismiss the mail composition view. Implementation of this method is optional, but expected.

If the user has opted to send the email created by this interface, that email should be queued in the user’s Mail program by the time this method is called. If an error occurred while queueing the email message, the `error` parameter contains an error object that indicates the type of failure that occurred.

## Parameters

- `controller`: The view controller object that manages the mail composition view.
- `result`: The result of the user’s action.
- `error`: If an error occurred, this parameter contains an error object with information about the type of failure.

## See Also

- [enum MFMailComposeResult](mfmailcomposeresult.md)
  Result codes returned when the mail composition interface is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate/mailcomposecontroller(_:didfinishwith:error:))*