# options

**Framework**: StoreKit  
**Kind**: property

The subscription options to merchandise within a section.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var options: [SubscriptionStoreControlStyleConfiguration.Option]
```

#### Discussion

This property represents the main content of a section. The view your style creates needs to provide a control to subscribe to each option in the array.

Use the properties of each [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) value to declare your control style, and use the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method in response to a subscribe interaction.

> 💡 **Tip**:  Use [`SubscriptionOptionSection`](subscriptionoptionsection.md) to configure the contents of a section when creating a [`SubscriptionStoreView`](subscriptionstoreview.md).

 Use [`SubscriptionOptionSection`](subscriptionoptionsection.md) to configure the contents of a section when creating a [`SubscriptionStoreView`](subscriptionstoreview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section/options)*