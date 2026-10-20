# authenticationToken

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The authentification token supplied to your web service.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var authenticationToken: String { get set }
```

```objc
@property (nonatomic, copy) NSString * authenticationToken;
```

## See Also

### Identifying and authenticating the order
- [var orderIdentifier: String](./orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [var orderTypeIdentifier: String](./ordertypeidentifier.md)
  An identifier for the order type associated with the order.
- [var webServiceURL: URL](./webserviceurl.md)
  The URL for your web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails/authenticationtoken)*