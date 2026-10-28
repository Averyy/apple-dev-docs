# SKReceiptPropertyIsVolumePurchase

**Framework**: StoreKit  
**Kind**: var  
**Role**: Global Variable

A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
let SKReceiptPropertyIsVolumePurchase: String
```

```c
extern NSString * const SKReceiptPropertyIsVolumePurchase;
```

## Discussion

This key’s value is an instance of [`NSNumber`](../Foundation/nsnumber.md) that the system interprets as a Boolean value that indicates whether the receipt is a Volume Purchase Plan receipt.

## See Also

### Receipt Properties and Keys
- [var receiptProperties: [String : Any]?](./skreceiptrefreshrequest/receiptproperties.md)
  The properties of the receipt.
- [let SKReceiptPropertyIsExpired: String](./skreceiptpropertyisexpired.md)
  A key with a value that indicates whether the receipt is in an expired state.
- [let SKReceiptPropertyIsRevoked: String](./skreceiptpropertyisrevoked.md)
  A key with a value that indicates whether the receipt is in a revoked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptpropertyisvolumepurchase)*