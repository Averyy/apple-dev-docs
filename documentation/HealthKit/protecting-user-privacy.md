# Protecting user privacy

**Framework**: HealthKit

Respect and safeguard your user’s privacy.

#### Overview

Because health data can be sensitive, HealthKit provides users with fine-grained control over the information that apps can share. The user must explicitly grant each app permission to read and write data to the HealthKit store. Users can grant or deny permission separately for each type of data.

For example, a user could let your app read step count data, but prevent it from reading blood glucose levels. To prevent possible information leaks, an app isn’t aware when the user denies permission to read data. From the app’s point of view, no data of that type exists.

> ❗ **Important**:  Apps must include usage descriptions, or it will crash when you request authorization to access HealthKit data. Include the [`NSHealthShareUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthShareUsageDescription) key to read, and [`NSHealthUpdateUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthUpdateUsageDescription) key to write data to Healthkit. For projects created using Xcode 13 or later, set these keys in the Target Properties list on the app’s Info tab. For projects created with Xcode 12 or earlier, set these keys in the apps `Info.plist` file. For more information, see [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).

##### Access Encrypted Data

The user’s device stores all HealthKit data locally. For security, the device encrypts the HealthKit store when the user locks the device. As a result, your app may not be able to read data from the store when it runs in the background. However, your app can still write to the store, even when the phone is locked. HealthKit temporarily caches the data and saves it to the encrypted store as soon as the user unlocks the phone.

##### Specify How Your App Uses the Health Data

In addition, your app must not access the HealthKit APIs unless the use is for health or fitness purposes and this usage is clear in both your marketing text and your user interface. Specifically, the following guidelines apply to all HealthKit apps:

- Your app may not use information gained through the use of the HealthKit framework for advertising or similar services. Note that you may still serve advertising in an app that uses the HealthKit framework, but you can’t use data from the HealthKit store to serve ads.
- You must not disclose any information gained through HealthKit to a third party without express permission from the user. Even with permission, you can only share information to a third party if they also provide a health or fitness service to the user.
- You can’t sell information gained through HealthKit to advertising platforms, data brokers, or information resellers.
- If the user consents, you may share their HealthKit data with a third party for medical research.
- You must clearly disclose to the user how you and your app will use their HealthKit data.

##### Provide a Privacy Policy

You must also provide a privacy policy for any app that uses the HealthKit framework. You can find guidance on creating a privacy policy at the following sites:

- Personal Health Record model (for non-HIPAA apps): [`http://www.healthit.gov/policy-researchers-implementers/personal-health-record-phr-model-privacy-notice`](https://developer.apple.comhttp://www.healthit.gov/policy-researchers-implementers/personal-health-record-phr-model-privacy-notice)
- HIPAA model (for HIPAA covered apps): [`https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/model-notices-privacy-practices/index.html`](https://developer.apple.comhttps://www.hhs.gov/hipaa/for-professionals/privacy/guidance/model-notices-privacy-practices/index.html)

These models, developed by the Office of the National Coordinator for Health Information Technology (ONC), are designed to improve user experience and comprehension with plain language and approachable designs that explain how your app collects and shares user data. These models aren’t intended to replace a web-based privacy policy, and developers should consult ONC guidance regarding which model is appropriate for a given app. These models are provided for your reference only, and Apple expressly disclaims all liability for your use of such models.

> **Note**:  It’s essential that you understand Apple’s requirements for working with HealthKit and the user’s health-related data. To learn about these requirements, see the HealthKit section in [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/) and the relevant sections in the [`Apple Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/support/terms/apple-developer-program-license-agreement/). The App Store Review Guidelines are also available from the [`App Review`](https://developer.apple.comhttps://developer.apple.com/app-store/review/) page. For additional technical information about working with sensitive user data, see [`Preparing your UI to run in the background`](https://developer.apple.com/documentation/UIKit/preparing-your-ui-to-run-in-the-background).

## See Also

- [About the HealthKit framework](about-the-healthkit-framework.md)
  Learn about the architecture and design of the HealthKit framework.
- [Setting up HealthKit](setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [Authorizing access to health data](authorizing-access-to-health-data.md)
  Request permission to read and share data in your app.
- [HealthKit updates](../Updates/HealthKit.md)
  Learn about important changes to HealthKit.
- [HealthKitUI](../healthkitui/healthkitui.md)
  Display user interface that enables a person to view and interact with their health data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/protecting-user-privacy)*