# receiptProperties

**Framework**: StoreKit  
**Kind**: property

The properties of the receipt.

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
var receiptProperties: [String : Any]? { get }
```

#### Discussion

Receipt properties include [`SKReceiptPropertyIsExpired`](skreceiptpropertyisexpired.md), [`SKReceiptPropertyIsRevoked`](skreceiptpropertyisrevoked.md), and [`SKReceiptPropertyIsVolumePurchase`](skreceiptpropertyisvolumepurchase.md).

## See Also

- [let SKReceiptPropertyIsExpired: String](skreceiptpropertyisexpired.md)
  A key with a value that indicates whether the receipt is in an expired state.
- [let SKReceiptPropertyIsRevoked: String](skreceiptpropertyisrevoked.md)
  A key with a value that indicates whether the receipt is in a revoked state.
- [let SKReceiptPropertyIsVolumePurchase: String](skreceiptpropertyisvolumepurchase.md)
  A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/receiptproperties)*