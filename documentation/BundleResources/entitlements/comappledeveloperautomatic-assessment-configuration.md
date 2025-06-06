# com.apple.developer.automatic-assessment-configuration

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app may create an assessment session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- macOS 10.15.4+

#### Discussion

Use an [`AEAssessmentSession`](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration/AEAssessmentSession) instance to put a device into a state that prevents users from accessing certain system features during high-stakes assessment activities, such as administering an exam. Your app needs the [`com.apple.developer.automatic-assessment-configuration`](entitlements/com.apple.developer.automatic-assessment-configuration.md) entitlement to create an assessment session.

To add the entitlement to your app, set the entitlement’s type to Boolean in the Xcode property list editor, and the corresponding value to `YES`.

![A screenshot of Xcode with a project’s entitlements file in the property list editor, showing the com.apple.developer.automatic-assessment-configuration entitlement.](https://docs-assets.developer.apple.com/published/55ccfc9accd23ff31a26e363d366dfc9/media-3540004%402x.png)

Before your app can use this entitlement, you must first get permission to use it. Request permission by filling in the [`Automatic Assessment Configuration Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/automatic-assessment-configuration/) form.

> ❗ **Important**:  If your app has a deployment target earlier than macOS 11, to use the [`com.apple.developer.automatic-assessment-configuration`](entitlements/com.apple.developer.automatic-assessment-configuration.md) entitlement, your app also needs the `com.apple.security.temporary-exception.mach-lookup.global-name` entitlement. Add this to your app’s entitlements file with a corresponding value that’s an array of strings containing the string `com.apple.assessmentagent`.

 If your app has a deployment target earlier than macOS 11, to use the [`com.apple.developer.automatic-assessment-configuration`](entitlements/com.apple.developer.automatic-assessment-configuration.md) entitlement, your app also needs the `com.apple.security.temporary-exception.mach-lookup.global-name` entitlement. Add this to your app’s entitlements file with a corresponding value that’s an array of strings containing the string `com.apple.assessmentagent`.

## See Also

- [ClassKit Environment Entitlement](entitlements/com.apple.developer.classkit-environment.md)
  The ClassKit development or production environment for an education app that works with the Schoolwork app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.automatic-assessment-configuration)*