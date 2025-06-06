# buyProduct(productIdentifier:)

**Framework**: StoreKit Test  
**Kind**: method

Simulates buying an in-app purchase or subscription outside the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
func buyProduct(productIdentifier: String) throws
```

#### Discussion

After calling this function, handle the new transaction in your payment queue.

## Parameters

- `productIdentifier`: Product identifier of the in-app purchase.

## See Also

- [func refundTransaction(identifier: Int) throws](sktestsession/refundtransaction(identifier:).md)
  Simulates a refund for an in-app purchase that completes outside of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/buyproduct(productidentifier:))*