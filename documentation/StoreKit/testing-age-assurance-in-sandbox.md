# Testing Age Assurance in Sandbox

**Framework**: StoreKit

Check that your app responds correctly to Age Assurance scenarios and consent revocation using the Sandbox environment.

#### Overview

You can provide people the ability to make decisions about who can access your app, or parts of your app. [`Declared Age Range`](https://developer.apple.com/documentation/DeclaredAgeRange) API enables you to request people’s age and create custom experiences based on the information they share, and [`PermissionKit`](https://developer.apple.com/documentation/PermissionKit) gives you the ability to provide parents or guardians the opportunity to decide if their child can access your app. Make sure your app implements age restrictions and processes permission revocation as parents or guardians instruct.

In the Sandbox environment you can test how your app responds to various age range scenarios, location-based restrictions, approval state changes, and consent revocation. Focus on testing age range variations across your target audience, and consider regulatory compliance in different regions.

##### Navigate to Your Sandbox Apple Account Settings

1. Confirm that you have enabled Developer Mode. If you haven’t, see [`Enabling Developer Mode on a device`](https://developer.apple.com/documentation/Xcode/enabling-developer-mode-on-a-device).
2. Open Settings and select Developer.
3. Scroll down to Sandbox Apple Account.
4. If you’re not logged in to an account, select Sign In to authenticate yourself.
5. Once you’ve authenticated, select your Apple Account.

##### Test Age Assurance on Device

1. Follow the steps from [`Navigate to your Sandbox Apple Account settings`](https://developer.apple.com#navigate-to-your-sandbox-apple-account-settings).
2. In the Sandbox Apple Account modal, select Manage.
3. Scroll down and select Age Assurance or Revoke App Consent.

You can also change these settings in App Store Connect.

When you select a scenario, the Declared Age Range API returns the corresponding [`upperBound`](https://developer.apple.com/documentation/DeclaredAgeRange/AgeRangeService/AgeRange/upperBound), [`lowerBound`](https://developer.apple.com/documentation/DeclaredAgeRange/AgeRangeService/AgeRange/lowerBound), and [`ageRangeDeclaration`](https://developer.apple.com/documentation/DeclaredAgeRange/AgeRangeService/AgeRange/ageRangeDeclaration) values, and PermissionKit returns the associated response status. Refer to the following table to check the specific values returned for each test case.

> **Note**: The age ranges in the test case are inclusive, meaning that all the ages between and including that age qualify as valid inputs in the test case.

| Test case | Lower bound | Upper bound | Age declaration | Significant app update notification | PermissionKit response |
| --- | --- | --- | --- | --- | --- |
| Under 13, approved | — | 12 | [`guardianPaymentChecked`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardianpaymentchecked) | True | [`approve`](https://developer.apple.com/documentation/PermissionKit/PermissionChoice/approve) |
| Ages 13 - 15, approved | 13 | 15 | [`guardianPaymentChecked`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardianpaymentchecked) | True | [`approve`](https://developer.apple.com/documentation/PermissionKit/PermissionChoice/approve) |
| Ages 16 - 17, declined | 16 | 17 | [`guardianPaymentChecked`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardianpaymentchecked) | True | [`decline`](https://developer.apple.com/documentation/PermissionKit/PermissionChoice/decline) |
| 18+, self declared | 18 | — | [`selfDeclared`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/selfdeclared) | False | [`AskError.systemError(underlyingError:)`](https://developer.apple.com/documentation/PermissionKit/AskError/systemError(underlyingError:)) |
| 18+, payment checked | 18 | — | [`paymentChecked`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/paymentchecked) | False | [`AskError.systemError(underlyingError:)`](https://developer.apple.com/documentation/PermissionKit/AskError/systemError(underlyingError:)) |

Check the `AgeRangeDeclaration` field in your Declared Age Range API responses to determine status.

##### Test App Consent Revocation

To test the notification when a parent or guardian revokes access to your app on behalf of their child, follow these steps:

1. Follow the steps from [`Navigate to your Sandbox Apple Account settings`](https://developer.apple.com#navigate-to-your-sandbox-apple-account-settings).
2. In the Sandbox Apple Account modal, select Manage.
3. Scroll down and select Revoke App Consent.
4. Enter your app’s Bundle ID (for example, com.example.bundle).
5. Tap Revoke Consent to simulate the revocation.
6. Confirm that the system displays “Notification Triggered” with the message “A notification will be sent to the developer server soon.”

If you have [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) enabled, your server receives a `RESCIND_CONSENT` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType). The notification payload includes an [`appData`](https://developer.apple.com/documentation/AppStoreServerNotifications/appData) object with app metadata, including the `bundleId` and `environment` fields that help you check the notification applies to the correct app and test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox)*