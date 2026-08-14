# Testing age assurance in sandbox

**Framework**: StoreKit

Check that your app responds correctly to age assurance scenarios and consent revocation using the sandbox environment.

#### Overview

You can provide parents and guardians with the ability to make decisions about whether their child can continue to access your app or parts of your app. [`Declared Age Range`](https://developer.apple.com/documentation/declaredagerange) API enables you to request people’s age and create custom experiences based on the information they share, and [`PermissionKit`](https://developer.apple.com/documentation/permissionkit) gives you the ability to provide parents or guardians the opportunity to decide if their child can continue using your app or parts of your app after a significant update. Make sure your app implements age restrictions and processes permission revocation as parents or guardians instruct.

In the sandbox environment you can test how your app responds to various age range scenarios, location-based restrictions, approval state changes, and consent revocation. Focus on testing age range variations across your target audience, and consider regulatory compliance in different regions.

##### Navigate to Your Sandbox Apple Account Settings

1. Confirm that you have enabled Developer Mode. If you haven’t, see [`Enabling Developer Mode on a device`](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device).
2. Open Settings and select Developer.
3. Scroll down to Sandbox Apple Account.
4. If you’re not logged in to an account, select Sign In to authenticate yourself.
5. Once you’ve authenticated, select your Apple Account.

##### Test Age Assurance on Device

1. Follow the steps from “Navigate to your Sandbox Apple Account.”
2. In the Sandbox Apple Account modal, select Manage.
3. Scroll down and select Age Assurance or Revoke App Consent.

When you select a scenario, the Declared Age Range API returns the corresponding [`upperBound`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/upperbound), [`lowerBound`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/lowerbound), and [`ageRangeDeclaration`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/agerangedeclaration) values, and PermissionKit returns the associated response status. Refer to the following table to check the specific values returned for each test case.

> **Note**: The age ranges in the test case are inclusive, meaning that all the ages between and including that age qualify as valid inputs in the test case.

| Test case | Lower bound | Upper bound | Age declaration | Significant app update notification | PermissionKit response |
| --- | --- | --- | --- | --- | --- |
| Under 13, significant change approved | — | 12 | [`guardianDeclared`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardiandeclared) | True | [`approve`](https://developer.apple.com/documentation/permissionkit/permissionchoice/approve) |
| 13 - 15, significant change approved | 13 | 15 | [`guardianDeclared`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardiandeclared) | True | [`approve`](https://developer.apple.com/documentation/permissionkit/permissionchoice/approve) |
| 16 - 17, significant change declined | 16 | 17 | [`guardianDeclared`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/guardiandeclared) | True | [`decline`](https://developer.apple.com/documentation/permissionkit/permissionchoice/decline) |
| 18+, age not confirmed, significant change not applicable | 18 | — | [`selfDeclared`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/selfdeclared) | False | [`AskError.notAvailable`](https://developer.apple.com/documentation/permissionkit/askerror/notavailable) |
| 18+, age confirmed, significant change not applicable | 18 | — | [`confirmed`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/confirmed) | False | [`AskError.notAvailable`](https://developer.apple.com/documentation/permissionkit/askerror/notavailable) |
| 18+, age confirmed, significant change applicable | 18 | — | [`confirmed`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/confirmed) | True | [`AskError.notAvailable`](https://developer.apple.com/documentation/permissionkit/askerror/notavailable) |

> **Note**: For 18+ test cases, PermissionKit throws `AskError.notAvailable` rather than returning a `PermissionChoice`. Calling `AskCenter.ask(_:)` for an adult user throws this error because they don’t meet the requirements for parental permission requests.

Check the `AgeRangeDeclaration` field in your Declared Age Range API responses to determine status.

##### Test App Consent Revocation

To test the notification when a parent or guardian revokes access to your app on behalf of their child, follow these steps:

1. Follow the steps from “Navigate to your Sandbox Apple Account.”
2. In the Sandbox Apple Account modal, select Manage.
3. Scroll down and select Revoke App Consent.
4. Enter your app’s Bundle ID (for example, com.example.bundle).
5. Tap Revoke Consent to simulate the revocation.
6. Confirm that the system displays “Notification Triggered” with the message “A notification will be sent to the developer server soon.”

If you have [`App Store Server Notifications V2`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) enabled, your server receives a `RESCIND_CONSENT` [`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype). The notification payload includes an [`appData`](https://developer.apple.com/documentation/appstoreservernotifications/appdata) object with app metadata, including the `bundleId` and `environment` fields that help you check the notification applies to the correct app and test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox)*