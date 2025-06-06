# PKSuppressionRequestToken

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: typealias

A token that represents a request to suppress the automatic presentation of payment passes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias PKSuppressionRequestToken = Int
```

#### Discussion

You receive a suppression request token when you begin suppressing the automatic presentation of passes. Use the token to end the suppression and reenable Apple Pay.

## See Also

- [func present(PKSecureElementPass)](pkpasslibrary/present(_:)-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](pkpasslibrary/issuppressingautomaticpasspresentation.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:).md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuppressionrequesttoken)*