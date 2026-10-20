# init(receiptProperties:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates a receipt refresh request with optional properties.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Transaction.all and AppTransaction.shared.

## Declaration

```swift
init(receiptProperties properties: [String : Any]?)
```

```objc
- (instancetype) initWithReceiptProperties:(NSDictionary<NSString *,id> *) properties;
```

## Mentions

- [Restoring purchased products](../restoring-purchased-products.md)

#### Return Value

The initialized request.

#### Discussion

In the sandbox environment, you can initialize a receipt with any combination of properties to test the state transitions related to Volume Purchase Plan receipts. Set the `properties` when you call this initializer.

## Parameters

- `properties`: In the test environment, the properties that the new receipt is to have. For keys, see Receipt Properties and Keys.

  In the production environment, set this parameter to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/init(receiptproperties:))*