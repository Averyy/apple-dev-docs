# Replacing a Game Center app

**Framework**: App Store Connect API  
**Role**: Article

Replace an existing Game Center app with a new one that belongs to the same Game Center and app groups as the original.

## Overview

In iOS and iPadOS 27.3 and later, you can replace a Game Center app using a prioritized list of app identifiers associated with your developer account that share the original’s app group and Game Center group with the new app.

## Offer to replace an app with an updated version

On the first run of the replacement app, the system offers to migrate the on-device settings and data from the existing app, and then to delete the existing app upon completion. If a person accepts this offer, the migration process starts, and when the process completes the system deletes the existing app.

The data the system migrates includes leaderboards, achievements, player scores, and progress.

If a person launching the newer app declines the replacement offer, the existing app and the new app remain installed on the device and able to access their respective versions of game resources.

## Provide a list of app identifiers

On the first launch of an app, the system enumerates the identifiers in the order presented in the property list you provide in the entitlement. For the first enumerated identifier that matches an app someone has already installed on the device, the system gives the person the option of replacing the app with a new app that inherits the older appʼs Game Center data and settings. If the person agrees to the replacement, the system deletes the older app. The person can access their Game Center data in the new app.

The app replacement offer process is a first-run activity and runs only once.

## Adopt the capability

To adopt this capability, follow these steps:

1. Request access to the App Replacement entitlement; for additional information, see [`App Replacement`](../BundleResources/entitlements/com.apple.developer.superseded-application-identifiers.md).
2. Add both the existing and the replacement apps to the same Game Center group in App Store Connect. Both apps must be from the same developer account. For information on adopting Game Center groups, see [Overview of Game Center groups](https://developer.apple.com/help/app-store-connect/configure-game-center/overview-of-game-center-groups/).
3. Obtain the app identifier for the existing app from the app’s record in App Store Connect.
4. Add the [`App Replacement`](../BundleResources/entitlements/com.apple.developer.superseded-application-identifiers.md) entitlement to the replacement app’s capabilities and add the existing app’s identifier to the property list as described in the App Replacement entitlement documentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/replacing-an-app)*