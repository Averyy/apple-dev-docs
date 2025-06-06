# appTransactionID

**Framework**: StoreKit  
**Kind**: property

The unique identifier of the app download transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var appTransactionID: String { get }
```

#### Discussion

The App Store server APIs and StoreKit provide this value in several APIs. For more information, see [`appTransactionID`](apptransaction/apptransactionid.md) in [`AppTransaction`](apptransaction.md).

## See Also

- [var appAccountToken: UUID?](product/subscriptioninfo/renewalinfo/appaccounttoken.md)
  The app account token you provided during the subscription purchase, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/apptransactionid)*