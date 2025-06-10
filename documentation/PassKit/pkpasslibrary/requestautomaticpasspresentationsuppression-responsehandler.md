# requestAutomaticPassPresentationSuppression(responseHandler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Prevents the device from automatically displaying the Apple Pay interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
class func requestAutomaticPassPresentationSuppression(responseHandler: @escaping (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken
```

#### Return Value

A [`PKPassLibrary`](pkpasslibrary.md) value that represents this request. Use this token to end the suppression of Apple Pay passes.

#### Discussion

If the device doesn’t support this feature, this method fails immediately and returns a token value of `0`. However, PassKit still calls the response handler.

#### Discussion

Use this method only in apps that must stay in the foreground when operating near NFC or other RF readers. This method prevents the device from automatically displaying the Apple Pay passes when it detects a compatible reader. This suppression occurs only while the app is in the foreground. The system automatically reenables the Apple Pay interface when the app goes to the background. If the app resumes, the system automatically suppresses the Apple Pay interface again.

This method operates asynchronously, and schedules the request and returns immediately. The system performs the actual request on a background thread, and after it completes, the system calls the response handler on an arbitrary queue and provides the result.

The first time the system calls this method, it alerts the user that Apple Pay is unavailable. This alert doesn’t display again until you uninstall and reinstall the app.

> ❗ **Important**:  This method requires a special entitlement from Apple. If the entitlement isn’t present, the request fails with a [`PKPassLibrary`](pkpasslibrary.md) result. For more information, see [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Parameters

- `responseHandler`: The response handler for the request.

## See Also

- [func present(PKSecureElementPass)](pkpasslibrary/present(_:)-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](pkpasslibrary/issuppressingautomaticpasspresentation.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [enum PKAutomaticPassPresentationSuppressionResult](pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:))*