# buyProduct(productIdentifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Simulates buying an Apple In-App Purchase or subscription outside the app.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use the Swift API: SKTestSession.buyProduct(identifier:, options:)

## Declaration

```swift
func buyProduct(productIdentifier: String) throws
```

```objc
- (BOOL) buyProductWithIdentifier:(NSString *) productIdentifier error:(NSError **) error;
```

#### Discussion

After calling this function, handle the new transaction in your payment queue.

## Parameters

- `productIdentifier`: Product identifier of the Apple In-App Purchase.

## See Also

### Testing externally performed transactions
- [func refundTransaction(identifier: Int) throws](./refundtransaction%28identifier%29.md)
  Simulates a refund for an Apple In-App Purchase that completes outside of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/buyproduct(productidentifier:))*