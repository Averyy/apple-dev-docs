# init(receiptProperties:)

**Framework**: StoreKit  
**Kind**: init

Creates a receipt refresh request with optional properties.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
init(receiptProperties properties: [String : Any]?)
```

## Mentions

- [Restoring purchased products](restoring-purchased-products.md)

#### Return Value

The initialized request.

#### Discussion

In the sandbox environment, you can initialize a receipt with any combination of properties to test the state transitions related to Volume Purchase Plan receipts. Set the `properties` when you call this initializer.

## Parameters

- `properties`: In the production environment, set this parameter to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/init(receiptproperties:))*