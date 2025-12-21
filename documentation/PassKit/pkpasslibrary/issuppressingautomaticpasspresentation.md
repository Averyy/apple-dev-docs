# isSuppressingAutomaticPassPresentation()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
class func isSuppressingAutomaticPassPresentation() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the system suppresses Apple Pay passes; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func present(PKSecureElementPass)](pkpasslibrary/present(_:)-9467u.md)
  Presents a Secure Element pass.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:).md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/issuppressingautomaticpasspresentation())*