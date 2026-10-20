# orderTypeIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An identifier for the order type associated with the order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var orderTypeIdentifier: String { get set }
```

```objc
@property (nonatomic, copy) NSString * orderTypeIdentifier;
```

## See Also

### Identifying and authenticating the order
- [var authenticationToken: String](./authenticationtoken.md)
  The authentification token supplied to your web service.
- [var orderIdentifier: String](./orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [var webServiceURL: URL](./webserviceurl.md)
  The URL for your web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails/ordertypeidentifier)*