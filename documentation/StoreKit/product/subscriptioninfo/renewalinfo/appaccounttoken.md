# appAccountToken

**Framework**: StoreKit  
**Kind**: property

The app account token you provided during the subscription purchase, if one exists.

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
var appAccountToken: UUID? { get }
```

#### Discussion

If you include an app account token in the purchase options when the customer purchases or changes the subscription,  this property is the app account token you provide. If you don’t provide an app account token, this property is `nil`.

## See Also

- [var appTransactionID: String](product/subscriptioninfo/renewalinfo/apptransactionid.md)
  The unique identifier of the app download transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/appaccounttoken)*