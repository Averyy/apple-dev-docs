# subscribe()

**Framework**: StoreKit  
**Kind**: method

Initiates a purchase when a customer activates a control to subscribe to the option.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func subscribe()
```

#### Discussion

Call the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method within your custom style when the customer chooses to make a purchase.

> ❗ **Important**:  Don’t call purchase methods, such as `Product/purchase(confirmIn:options:)`, on the [`subscription`](subscriptionstorecontrolstyleconfiguration/option/subscription.md) property from your custom style.

 Don’t call purchase methods, such as `Product/purchase(confirmIn:options:)`, on the [`subscription`](subscriptionstorecontrolstyleconfiguration/option/subscription.md) property from your custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscribe())*