# tokenNotificationURL

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A URL to receive life-cycle notifications for the merchant-specific payment token the system issues for the request, if applicable.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var tokenNotificationURL: URL? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSURL * tokenNotificationURL;
```

## Discussion

If you don’t set this property, the framework doesn’t send notifications when life-cycle changes occur for the token, for example when the framework deletes the token.

## See Also

### Managing payment tokens
- [var managementURL: URL](./managementurl.md)
  A URL that links to a page on your web site where the user can manage the payment method for the deferred payment, including deleting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/tokennotificationurl)*