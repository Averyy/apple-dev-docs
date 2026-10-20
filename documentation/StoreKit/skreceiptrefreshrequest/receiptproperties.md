# receiptProperties

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The properties of the receipt.

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
var receiptProperties: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * receiptProperties;
```

#### Discussion

Receipt properties include [`SKReceiptPropertyIsExpired`](../skreceiptpropertyisexpired.md), [`SKReceiptPropertyIsRevoked`](../skreceiptpropertyisrevoked.md), and [`SKReceiptPropertyIsVolumePurchase`](../skreceiptpropertyisvolumepurchase.md).

## See Also

### Receipt Properties and Keys
- [let SKReceiptPropertyIsExpired: String](../skreceiptpropertyisexpired.md)
  A key with a value that indicates whether the receipt is in an expired state.
- [let SKReceiptPropertyIsRevoked: String](../skreceiptpropertyisrevoked.md)
  A key with a value that indicates whether the receipt is in a revoked state.
- [let SKReceiptPropertyIsVolumePurchase: String](../skreceiptpropertyisvolumepurchase.md)
  A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/receiptproperties)*