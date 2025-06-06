# SKReceiptPropertyIsVolumePurchase

**Framework**: StoreKit  
**Kind**: var

A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.

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
let SKReceiptPropertyIsVolumePurchase: String
```

#### Discussion

This key’s value is an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that the system interprets as a Boolean value that indicates whether the receipt is a Volume Purchase Plan receipt.

## See Also

- [var receiptProperties: [String : Any]?](skreceiptrefreshrequest/receiptproperties.md)
  The properties of the receipt.
- [let SKReceiptPropertyIsExpired: String](skreceiptpropertyisexpired.md)
  A key with a value that indicates whether the receipt is in an expired state.
- [let SKReceiptPropertyIsRevoked: String](skreceiptpropertyisrevoked.md)
  A key with a value that indicates whether the receipt is in a revoked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptpropertyisvolumepurchase)*