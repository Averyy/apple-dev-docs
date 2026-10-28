# subscribe()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Initiates a purchase when a customer activates a control to subscribe to the option.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func subscribe()
```

## Discussion

Call the [`subscribe()`](./subscribe%28%29.md) method within your custom style when the customer chooses to make a purchase.

> ❗ **Important**:  Don’t call purchase methods, such as [`purchase(confirmIn:options:)`](../../product/purchase%28confirmin,options%29-8eai6.md), on the [`subscription`](./subscription.md) property from your custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscribe())*