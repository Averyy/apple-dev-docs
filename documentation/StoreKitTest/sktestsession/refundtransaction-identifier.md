# refundTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Simulates a refund for an in-app purchase that completes outside of the app.

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

#### Discussion

In the testing environment, the system always approves refund requests, and processes them immediately. You can choose the reason for the refund by using [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(in:)-9k0pj) in your app and selecting a reason. (Your app may also use [`beginRefundRequest(for:in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph), [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(in:)-63bvd), or [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(in:)-63bvd).  If your app uses SwiftUI, it may use [`refundRequestSheet(for:isPresented:onDismiss:)`](https://developer.apple.com/documentation/swiftui/view/refundrequestsheet(for:ispresented:ondismiss:)).) Otherwise, the refund reason defaults to [`other`](https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.struct/other).

After calling this function, handle the new transaction in [`updates`](https://developer.apple.com/documentation/storekit/transaction/updates) or in your payment queue. Look for the [`revocationDate`](https://developer.apple.com/documentation/storekit/transaction/revocationdate) and [`revocationReason`](https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.property) properties, which indicate the refund.

## Parameters

- `identifier`: The transaction [`identifier`](sktesttransaction/identifier.md) of an in-app purchase to get a refund.

## See Also

- [func buyProduct(productIdentifier: String) throws](sktestsession/buyproduct(productidentifier:).md)
  Simulates buying an in-app purchase or subscription outside the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/refundtransaction(identifier:))*