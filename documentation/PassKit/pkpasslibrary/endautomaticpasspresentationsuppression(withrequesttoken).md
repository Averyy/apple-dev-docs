# endAutomaticPassPresentationSuppression(withRequestToken:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Reenables the automatic display of the Apple Pay interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
class func endAutomaticPassPresentationSuppression(withRequestToken requestToken: PKSuppressionRequestToken)
```

```objc
+ (void) endAutomaticPassPresentationSuppressionWithRequestToken:(PKSuppressionRequestToken) requestToken;
```

#### Discussion

This method reenables the automatic presentation of Apple Pay passes when the device detects a compatible reader.

## Parameters

- `requestToken`: The token you receive when you call the [`PKPassLibrary`](../pkpasslibrary.md) method. If you pass in an invalid request token, the system ignores the end request.

## See Also

### Presenting and suppressing passes
- [func present(PKSecureElementPass)](./present%28_%29-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](./issuppressingautomaticpasspresentation%28%29.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](./requestautomaticpasspresentationsuppression%28responsehandler%29.md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](../pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [typealias PKSuppressionRequestToken](../pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:))*