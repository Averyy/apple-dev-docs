# PKAutomaticPassPresentationSuppressionResult

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

The result of an attempt to suppress automatic pass presentation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
enum PKAutomaticPassPresentationSuppressionResult
```

## Topics

### Constants
- [PKAutomaticPassPresentationSuppressionResult.notSupported](pkautomaticpasspresentationsuppressionresult/notsupported.md)
  The device doesn’t support the suppression of automatic pass presentation.
- [PKAutomaticPassPresentationSuppressionResult.alreadyPresenting](pkautomaticpasspresentationsuppressionresult/alreadypresenting.md)
  The device is already presenting passes.
- [PKAutomaticPassPresentationSuppressionResult.denied](pkautomaticpasspresentationsuppressionresult/denied.md)
  The user prevented the suppression, or an internal error occurred.
- [PKAutomaticPassPresentationSuppressionResult.cancelled](pkautomaticpasspresentationsuppressionresult/cancelled.md)
  The system canceled the suppression before calling the response handler.
- [PKAutomaticPassPresentationSuppressionResult.success](pkautomaticpasspresentationsuppressionresult/success.md)
  Suppression of automatic presentation successful.
### Initializers
- [init?(rawValue: UInt)](pkautomaticpasspresentationsuppressionresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func present(PKSecureElementPass)](pkpasslibrary/present(_:)-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](pkpasslibrary/issuppressingautomaticpasspresentation.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:).md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult)*