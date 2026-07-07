# init(_:)

**Framework**: StoreKit  
**Kind**: init

Creates a button with an automatic label that describes the subscription option and starts a subscribe interaction when someone selects the button.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ option: SubscriptionStoreControlStyleConfiguration.Option)
```

#### Discussion

You receive [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) values to initialize the subscribe button from the [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method of your custom subscription store control style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorebutton/init(_:))*