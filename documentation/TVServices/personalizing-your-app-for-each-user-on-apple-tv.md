# Personalizing Your App for Each User on Apple TV

**Framework**: TV Services

Use account-specific storage to segregate data on a multiuser system.

#### Overview

Multiple people can log in to accounts on a single Apple TV, and you can set up your app so each member of a household can use it with their own Apple TV account. When a user logs in, your app can access their preferences and GameCenter and iCloud data. If your app is also available on iOS or iPadOS, a user can pick up where they left off on their personal device as well.

If your app doesn’t include the `User Management` capability, the system runs your app as the default user, instead of the current user. If you design your app with individual profiles in a single shared account, consider [`Mapping Apple TV users to app profiles`](mapping-apple-tv-users-to-app-profiles.md) instead.

##### Access the Current Users Data

In most cases, managing each user’s data in their Apple account provides the best user experience, but it requires some support in your app. In order to provide a personalized experience in your app, enable the `Runs as Current User` privilege in the [`User Management Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.user-management) capability. This entitlement grants your app access to data for the current user in keychain, preferences, iCloud, and Game Center.

Implement [`applicationWillTerminate(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillTerminate(_:)) to save data in case a user switch occurs while your app is in the foreground. Make sure you’re using [`applicationWillResignActive(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillResignActive(_:)) to save data whenever the user switches away from your app.

##### Optimize Data Usage

When your app receives a push notification from CloudKit, use [`subscriptionOwnerUserRecordID`](https://developer.apple.com/documentation/CloudKit/CKNotification/subscriptionOwnerUserRecordID) to check whether the update is for the current user. If the notification is for another user on this device, you may choose to ignore the push, and get the data the next time the other user accesses your app.

## See Also

- [Supporting Multiple Users in Your tvOS App](supporting-multiple-users-in-your-tvos-app.md)
  Store separate data for each user with the new Runs as Current User capability.
- [Mapping Apple TV users to app profiles](mapping-apple-tv-users-to-app-profiles.md)
  Adapt the content of your app for the current viewer by using an entitlement and simplifying sign-in flows.
- [class TVUserManager](tvusermanager.md)
  An object that indicates how to store preferences for multiple people on a shared device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/personalizing-your-app-for-each-user-on-apple-tv)*