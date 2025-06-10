# sync()

**Framework**: StoreKit  
**Kind**: method

Synchronizes your app’s transaction information and subscription status with information from the App Store.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func sync() async throws
```

#### Discussion

Include some mechanism in your app, such as a Restore Purchases button, to let users restore their in-app purchases. In rare cases when a user suspects the app isn’t showing all the transactions, call [`sync()`](appstore/sync().md). By calling [`sync()`](appstore/sync().md), you force the app to obtain transaction information and subscription status from the App Store.

> ❗ **Important**:  Calling [`sync()`](appstore/sync().md)displays a system prompt that asks users to authenticate with their App Store credentials. Call this function only in response to an explicit user action, like tapping or clicking a button.

In regular operations, there’s no need to call [`sync()`](appstore/sync().md). StoreKit automatically keeps up to date transaction information and subscription status available to your app. When users reinstall your app or download it on a new device, the app automatically has all transactions available to it upon initial launch. There’s no need for users to ask your app to restore transactions — your app can immediately get the current entitlements using [`currentEntitlements`](transaction/currententitlements.md) and transaction history using [`all`](transaction/all.md). For more information about transactions, see [`Transaction`](transaction.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/sync())*