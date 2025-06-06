# present(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Presents a Secure Element pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func present(_ pass: PKSecureElementPass)
```

#### Discussion

Your app can only present provisioned passes. The library must contain `pass`. Otherwise, calling this method has no effect.

## Parameters

- `pass`: The Secure Element pass to present.

## See Also

- [class func isSuppressingAutomaticPassPresentation() -> Bool](pkpasslibrary/issuppressingautomaticpasspresentation.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:).md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/present(_:)-9467u)*