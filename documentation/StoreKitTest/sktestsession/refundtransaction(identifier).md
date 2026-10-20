# refundTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Simulates a refund for an Apple In-App Purchase that completes outside of the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func refundTransaction(identifier: Int) throws
```

```objc
- (BOOL) refundTransactionWithIdentifier:(NSUInteger) identifier error:(NSError **) error;
```

#### Discussion

In the testing environment, the system always approves refund requests, and processes them immediately. You can choose the reason for the refund by using [`beginRefundRequest(in:)`](../../StoreKit/transaction/beginrefundrequest%28in%29-9k0pj.md) in your app and selecting a reason. (Your app may also use [`beginRefundRequest(for:in:)`](../../StoreKit/transaction/beginrefundrequest%28for,in%29-65tph.md), [`beginRefundRequest(in:)`](../../StoreKit/transaction/beginrefundrequest%28in%29-63bvd.md), or [`beginRefundRequest(in:)`](../../StoreKit/transaction/beginrefundrequest%28in%29-63bvd.md).  If your app uses SwiftUI, it may use [`refundRequestSheet(for:isPresented:onDismiss:)`](../../SwiftUI/view/refundrequestsheet%28for,ispresented,ondismiss%29.md).) Otherwise, the refund reason defaults to [`other`](../../StoreKit/transaction/revocationreason-swift.struct/other.md).

After calling this function, handle the new transaction in [`updates`](../../StoreKit/transaction/updates.md) or in your payment queue. Look for the [`revocationDate`](../../StoreKit/transaction/revocationdate.md) and [`revocationReason`](../../StoreKit/transaction/revocationreason-swift.property.md) properties, which indicate the refund.

## Parameters

- `identifier`: The transaction [`identifier`](../sktesttransaction/identifier.md) of an Apple In-App Purchase to get a refund.

## See Also

### Testing externally performed transactions
- [func buyProduct(productIdentifier: String) throws](./buyproduct%28productidentifier%29.md)
  Simulates buying an Apple In-App Purchase or subscription outside the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/refundtransaction(identifier:))*