# SubscriptionStoreButton

**Framework**: StoreKit  
**Kind**: struct

A button for subscribing to an in-app subscription with a localized label and optional caption.

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
@preconcurrency struct SubscriptionStoreButton
```

#### Overview

When implementing custom subscription store control styles conforming to [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md), you can use this button to utilize the standard subscribe button as a component of the view you provide from [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md). The subscription store button automatically generates a localized label and optional caption for the corresponding subscription option. To configure a custom button label, use [`Button`](https://developer.apple.com/documentation/SwiftUI/Button) instead.

Standard subscription store control styles use the subscription store button. For example, the [`buttons`](subscriptionstorecontrolstyle/buttons.md) style creates a `SubscriptionStoreButton` instance for each subscription option.

> 💡 **Tip**:  Within the scope of your type conforming to [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md), you can spell `SubscriptionStoreButton` as `SubscribeButton` through the [`SubscriptionStoreControlStyle.SubscribeButton`](subscriptionstorecontrolstyle/subscribebutton.md) type alias.

 Within the scope of your type conforming to [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md), you can spell `SubscriptionStoreButton` as `SubscribeButton` through the [`SubscriptionStoreControlStyle.SubscribeButton`](subscriptionstorecontrolstyle/subscribebutton.md) type alias.

In iOS, macOS, visionOS and watchOS you can configure the button’s label by modifying it with `subscriptionStoreButtonLabel(_:)`. Some button label configurations cause the button to have a caption, for example .`displayName.singleLine`.

Because the `SubscriptionStoreButton` is composed of a SwiftUI [`Button`](https://developer.apple.com/documentation/SwiftUI/Button), you can also configure the button using other built-in view modifiers such as [`buttonStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonStyle(_:)-66fbx).

To create a `SubscriptionStoreButton`, provide a value of [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) to the [`init(_:)`](subscriptionstorebutton/init(_:).md) method. Get an option value from the required [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method on your [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md) implementation.

> ❗ **Important**:  Use `SubscriptionStoreButton` only in the view you return from the required [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method of [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md). Using `SubscriptionStoreButton` in other contexts is not supported.

 Use `SubscriptionStoreButton` only in the view you return from the required [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method of [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md). Using `SubscriptionStoreButton` in other contexts is not supported.

## Topics

### Creating a subscription store button
- [init(SubscriptionStoreControlStyleConfiguration.Option)](subscriptionstorebutton/init(_:).md)
  Creates a button with an automatic label that describes the subscription option and starts a subscribe interaction when someone selects the button.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct SubscriptionStorePicker](subscriptionstorepicker.md)
  A composite control with a picker for selecting a subscription option and a button for confirming the subscription.
- [struct SubscriptionStorePickerOption](subscriptionstorepickeroption.md)
  A subscription option within a subscription picker control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorebutton)*