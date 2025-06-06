# init(orderTypeIdentifier:orderIdentifier:webServiceURL:authenticationToken:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes a payment order details object with the identifier, web service URL, and authentication token you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(orderTypeIdentifier: String, orderIdentifier: String, webServiceURL: URL, authenticationToken: String)
```

## Parameters

- `orderTypeIdentifier`: An identifier for the order type associated with the order.
- `orderIdentifier`: A unique order identifier scoped to your order type identifier.
- `webServiceURL`: The URL of your web service.
- `authenticationToken`: The authentication token supplied to your web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails/init(ordertypeidentifier:orderidentifier:webserviceurl:authenticationtoken:))*