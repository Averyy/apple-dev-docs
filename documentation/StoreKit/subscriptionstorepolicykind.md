# SubscriptionStorePolicyKind

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The type of policy, such as the terms of service or privacy policies.

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
struct SubscriptionStorePolicyKind
```

## Overview

To set the destination of a policy button in a [`SubscriptionStoreView`](./subscriptionstoreview.md), use [`subscriptionStorePolicyDestination(url:for:)`](../SwiftUI/view/subscriptionstorepolicydestination%28url,for%29.md) or [`subscriptionStorePolicyDestination(for:destination:)`](../SwiftUI/view/subscriptionstorepolicydestination%28for,destination%29.md).

## Topics

### Getting policy types
- [static var privacyPolicy: SubscriptionStorePolicyKind](./subscriptionstorepolicykind/privacypolicy.md)
  The privacy policy type.
- [static var termsOfService: SubscriptionStorePolicyKind](./subscriptionstorepolicykind/termsofservice.md)
  The terms of service policy type.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Configuring the subscription store policies
- [func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind, destination: () -> some View) -> some View
](../SwiftUI/view/subscriptionstorepolicydestination%28for,destination%29.md)
  Configures a view as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyDestination(url: URL, for: SubscriptionStorePolicyKind) -> some View
](../SwiftUI/view/subscriptionstorepolicydestination%28url,for%29.md)
  Configures a URL as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View
](../SwiftUI/view/subscriptionstorepolicyforegroundstyle%28_%29.md)
  Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle) -> some View
](../SwiftUI/view/subscriptionstorepolicyforegroundstyle%28_,_%29.md)
  Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepolicykind)*