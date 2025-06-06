# finish()

**Framework**: StoreKit  
**Kind**: method

Indicates to the App Store that the app delivered the purchased content or enabled the service to finish the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func finish() async
```

## Mentions

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)

#### Discussion

Call [`finish()`](transaction/finish().md) to complete a transaction after you deliver the purchased content or enable the purchased service. For on-demand resources, don’t finish the transaction until the app completes downloading the resource or you’ve otherwise delivered the resource.

## See Also

- [static var unfinished: Transaction.Transactions](transaction/unfinished.md)
  A sequence that emits unfinished transactions for the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/finish())*