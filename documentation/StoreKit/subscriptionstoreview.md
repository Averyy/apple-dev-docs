# SubscriptionStoreView

**Framework**: StoreKit  
**Kind**: struct

A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionStoreView<Content> where Content : View
```

## Mentions

- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md)

#### Overview

A `SubscriptionStoreView` displays localized information about auto-renewable subscriptions, including their localized names, descriptions, and prices, as well as a purchase button.

Create a subscription store view by using one of the initializers and providing the following information:

- A subscription group identifier
- A collection of product identifiers
- A collection of product values you previously loaded from the App Store

If you provide a subscription group identifier or a collection of product identifiers, the subscription store view automatically loads the subscription data from the App Store, and updates the view when the data is available.

##### Provide a Background and a Decorative Icon

The subscription store view doesn’t draw a background by default. You can add a background as follows:

- To layer a background behind the view, use a view modifier, such as `background(alignment:content:)`.
- To set the container background of the subscription store using a view, use the `containerBackground(_:for:)` or `containerBackground(for:alignment:content:)` view modifier and specify a [`ContainerBackgroundPlacement`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement), such as [`subscriptionStoreHeader`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement/subscriptionStoreHeader).

You can optionally provide a view as a decorative icon next to each subscription option. Use the [`subscriptionStoreControlIcon(icon:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStoreControlIcon(icon:)) view modifier to set a view that decorates individual subscription options within a subscription store.

##### Order and Filter Subscriptions

If you create the subscription store view by providing a subscription group identifier, the system orders the subscription options according to their rank. If the customer is already subscribed, you may want to merchandise upgrade or crossgrade options. By default, the subscription store view lists all the subscriptions in the group. To hide certain subscription options, provide the `visibleRelationships` parameter in the initializer. For more information about the visible relationships, see [`Product.SubscriptionRelationship`](product/subscriptionrelationship.md).

If you create the subscription store view using one of the other initializers, the view orders the subscriptions according to the collection parameter’s order. The view excludes subscriptions that you don’t include in the collection parameter.

##### Add Terms of Service and Privacy Policies

The `SubscriptionStoreView` automatically displays buttons for the terms of service and privacy policy that you submit in App Store Connect. To override the destination of these buttons with a URL to custom terms of service and privacy policy pages, or a custom view, use the modifiers [`subscriptionStorePolicyDestination(url:for:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStorePolicyDestination(url:for:)) and [`subscriptionStorePolicyDestination(for:destination:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStorePolicyDestination(for:destination:)).

Use modifiers, such as [`subscriptionStorePolicyForegroundStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStorePolicyForegroundStyle(_:)), to customize the button’s style, for example, to make the text more readable against your store’s background.

##### Add Auxiliary Buttons

You can show auxiliary buttons in the subscription store using view modifiers. Specify the button’s visibility within the subscription store by using the [`storeButton(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/storeButton(_:for:)) view modifier.

If you offer your subscription through other services, you can configure the subscription store view to display a sign-in button. Use the [`subscriptionStoreSignInAction(_:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStoreSignInAction(_:)) modifier to set the function your app calls when someone uses the sign-in button.

The subscription store view automatically shows a Close button. To override this behavior, use the `storeButton(_:for:)` modifier to unconditionally show, or hide, the Close button.

##### Style the Subscription Store View

You can further customize the subscription store’s appearance using control styles. Use subscription store control styles to customize the display of subscription options, and how people interact with your store. To try out standard styles, such as [`PickerSubscriptionStoreControlStyle`](pickersubscriptionstorecontrolstyle.md), apply the style using the [`subscriptionStoreControlStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStoreControlStyle(_:)) modifier.

## Topics

### Creating subscription store views with automatic marketing content
- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship)](subscriptionstoreview/init(groupid:visiblerelationships:).md)
  Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(productIDs: some Collection<String>)](subscriptionstoreview/init(productids:).md)
  Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.
- [init(subscriptions: some Collection<Product>)](subscriptionstoreview/init(subscriptions:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.
### Creating subscription store views with custom marketing content
- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship, marketingContent: () -> Content)](subscriptionstoreview/init(groupid:visiblerelationships:marketingcontent:).md)
  Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.
- [init(productIDs: some Collection<String>, marketingContent: () -> Content)](subscriptionstoreview/init(productids:marketingcontent:).md)
  Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.
- [init(subscriptions: some Collection<Product>, marketingContent: () -> Content)](subscriptionstoreview/init(subscriptions:marketingcontent:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.
### Creating subscription store views with a hierarchichal structure
- [init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship, content: () -> C)](subscriptionstoreview/init(groupid:visiblerelationships:content:).md)
- [init<C>(productIDs: some Collection<String>, content: () -> C)](subscriptionstoreview/init(productids:content:).md)
- [init<C>(subscriptions: some Collection<Product>, content: () -> C)](subscriptionstoreview/init(subscriptions:content:).md)
### Supporting types
- [struct AutomaticSubscriptionStoreMarketingContent](automaticsubscriptionstoremarketingcontent.md)
  A view that represents the default marketing content for a subscription store.
- [struct SubscriptionStoreContentView](subscriptionstorecontentview.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct ProductView](productview.md)
  A view that merchandises an individual In-App Purchase product.
- [struct StoreView](storeview.md)
  A view that merchandises a collection of In-App Purchase products.
- [struct SubscriptionOfferView](subscriptionofferview.md)
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/Backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview)*