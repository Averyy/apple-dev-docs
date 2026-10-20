# webServiceURL

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The URL for your web service.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var webServiceURL: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * webServiceURL;
```

## See Also

### Identifying and authenticating the order
- [var authenticationToken: String](./authenticationtoken.md)
  The authentification token supplied to your web service.
- [var orderIdentifier: String](./orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [var orderTypeIdentifier: String](./ordertypeidentifier.md)
  An identifier for the order type associated with the order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails/webserviceurl)*