# autoRenewPreference

**Framework**: StoreKit  
**Kind**: property

The auto-renewable subscripton product that renews at the next billing cycle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var autoRenewPreference: Product? { get }
```

#### Discussion

Use the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) property to identify the subscription that renews in the next billing cycle, if there is one. The property is `nil` if the customer doesn’t have an auto-renewable subscription that renews in the next billing period. This indicates that the customer turned off the auto-renew preference, or that they don’t have a current subscription.

Display the subscription in the auto-renew preference only if it appears in the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) arrays. However, disable its [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) control so the customer doesn’t try to subscribe to it again, to prevent a system dialog that explains that the customer is already subscribed. The following code example shows how to check for the auto-renew preference and disable the subscribe functionality:

```swift
ForEach(configuration.options) { option in 
    Button(option.displayName, action: option.subscribe)
        .disabled(option.id == configuration.autoRenewPreference?.id)
}
```

> ❗ **Important**:  Don’t use the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) property to determine whether to grant access to a service. Always check the full transaction information before granting access to a paid service.

## See Also

- [var groupDisplayName: String](subscriptionstorecontrolstyleconfiguration/groupdisplayname.md)
  The localized display name of the subscription group that the subscription store view merchandises.
- [var allOptions: [Product]](subscriptionstorecontrolstyleconfiguration/alloptions.md)
  All subscription options in the subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/autorenewpreference)*