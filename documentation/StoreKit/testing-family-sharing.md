# Testing Family Sharing

**Framework**: StoreKit

Verify that your app handles auto-renewable subscriptions and non-consumable in-app purchases that family members share with Family Sharing.

#### Overview

Family Sharing lets people share access to auto-renewable subscriptions or non-consumables that have Family Sharing enabled with up to five family members. You can use Sandbox Test Families to test whether your app works with Family Sharing as expected.

> **Note**:  Changes that you make to product metadata in App Store Connect can take up to one hour to appear in the sandbox environment.

To test Family Sharing in your app:

- Ensure your in-app purchases are set up to support Family Sharing. For more information, see [`Turn on Family Sharing for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases).
- Create two or more Sandbox Apple Accounts to add to a Sandbox Test Family, or use existing accounts. A family group can have up to six members. For more information, see [`Create a Sandbox Apple Account`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids).
- Create the Sandbox Test Family in App Store Connect. For more information, see [`Create a Sandbox Test Family`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-id-settings#create-a-sandbox-test-family).
- To make testing easier, have a separate device to use for each test family member. You can also use a single device and sign in using each family member’s Sandbox Apple Account in turn.

##### Manage Sharing for the Sandbox Test Family

You can set the sharing status for each member of the Sandbox Test Family individually, as follows:

-  indicates the family member shares their in-app purchases with the Sandbox Test Family, and gets access to in-app purchases shared by family members.
-  indicates the family member isn’t sharing, and doesn’t get access to family-shared purchases. Changing the setting to Not Sharing revokes any family-shared purchases they have access to. In the test environment, turning off sharing is the equivalent of a family member leaving the group.

![The settings page titled Family Sharing. The top of the page has a label that reads Sandbox Family Members. A list box lists five Sandbox Apple Accounts that comprise the Sandbox Test Family. Each Apple Account has a label underneath that reads Sharing. A link below the list is labeled Stop Sharing Purchases. ](https://docs-assets.developer.apple.com/published/08ba8ae02734a6799040e16023c5eeeb/media-4312484%402x.png)

Modify the sharing status on the Family Sharing page in iOS by following these steps:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account.
3. On the popup sheet, select Manage.
4. On the Account Settings page, select Family Sharing.
5. Select a family member.
6. Select Stop Sharing Purchases or Start Sharing Purchases, as appropriate.

You can also change these settings in App Store Connect. For more information, see [`Manage a Sandbox Test Family`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-id-settings#manage-a-sandbox-test-family).

##### Test Sharing an in App Purchase in a Family Group

The two main test cases for Family Sharing are a family member gaining and losing access to family-shared purchases. You can simulate these situations as follows.

To test family members gaining access to a shared purchase:

1. Start with a Sandbox Test Family where members are sharing.
2. In your app, purchase a shareable product.
3. Open your app on a device signed in with the Sandbox Apple Account of another test family member.
4. Verify that your app receives a transaction for the shared purchase and unlocks the content for the family member. Note that the transaction has a [`familyShared`](transaction/ownershiptype-swift.struct/familyshared.md) ownership type.
5. When sharing auto-renewable subscriptions, if you have [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) enabled in the sandbox environment, your server receives a notification for each test family member that has sharing enabled. For more information, see the `SUBSCRIBED` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType).

##### Test Revoked Access to Shared in App Purchases

To test a family member losing access to shared purchases:

1. Start with a Sandbox Test Family with two or more members, and at least one shared purchase.
2. In Account Settings > Family Sharing, select a test family member that is receiving access to a shared in-app purchase.
3. Select Stop Sharing Purchases, and Stop Sharing to confirm.
4. The test family member loses accesses to shared purchases. Open your app using their Sandbox Apple Account and confirm that your app receives an updated transaction that includes a [`revocationDate`](transaction/revocationdate.md) and [`revocationReason`](transaction/revocationreason-swift.property.md).
5. If you have [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) enabled in the sandbox environment, your server receives a `REVOKE` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) for the test family member that has sharing disabled.

Note that you can also change the sharing status using App Store Connect instead of Account Settings in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-family-sharing)*