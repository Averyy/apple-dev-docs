# AutomaticSubscriptionStoreMarketingContent

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A view that represents the default marketing content for a subscription store.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AutomaticSubscriptionStoreMarketingContent
```

#### Overview

You don’t use this type directly. Instead, create a [`SubscriptionStoreView`](./subscriptionstoreview.md) using an initializer that doesn’t include a `marketingContent` parameter for providing custom marketing content.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Supporting types
- [struct SubscriptionStoreContentView](./subscriptionstorecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/automaticsubscriptionstoremarketingcontent)*