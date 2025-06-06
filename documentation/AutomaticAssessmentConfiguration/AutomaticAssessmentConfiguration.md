# Automatic Assessment Configuration

**Framework**: Automatic Assessment Configuration  
**Kind**: module

Enter single-app mode and prevent students from accessing specific system features while taking an exam.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+

#### Overview

Use the AutomaticAssessmentConfiguration framework to create an assessment session that limits access to system features. The session prevents a user from using the device to retrieve information beyond that which your app provides, or distributing sensitive information from within your app. This limited access helps you protect the integrity of an assessment, like an exam, conducted by your app.

Apps that use the AutomaticAssessmentConfiguration framework must have the [`com.apple.developer.automatic-assessment-configuration`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration) entitlement. With the entitlement set, use an instance of the [`AEAssessmentSession`](aeassessmentsession.md) class to start and stop assessment sessions.

A session provides protections by preventing access to desktop elements like:

- The Dock
- The Application Menu Bar
- Mission Control
- Notification Center
- Spaces other than the current one
- Other apps, except those that you selectively allow

Additionally, a session:

- Prevents screen recording and screen capture
- Disables Siri
- Stops media playing
- Allows network access for only your app
- Disables Handoff
- Clears the pasteboard buffer when starting and stopping the session

> **Note**:  If you publish an educational app that delivers exams to students, you can request permission to use the [`com.apple.developer.automatic-assessment-configuration`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration) entitlement by filling in the [`Automatic Assessment Configuration Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/automatic-assessment-configuration/) form.

 If you publish an educational app that delivers exams to students, you can request permission to use the [`com.apple.developer.automatic-assessment-configuration`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration) entitlement by filling in the [`Automatic Assessment Configuration Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/automatic-assessment-configuration/) form.

The framework reports an error if you try to start an assessment from an app running in visionOS.

## Topics

### Essentials
- [com.apple.developer.automatic-assessment-configuration](../BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration.md)
  A Boolean value that indicates whether an app may create an assessment session.
### Sessions
- [Preparing an educational assessment app for distribution](preparing-an-educational-assessment-app-for-distribution.md)
  Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](build-an-educational-assessment-app.md)
  Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- [class AEAssessmentConfiguration](aeassessmentconfiguration.md)
  Configuration information for an assessment session.
- [class AEAssessmentSession](aeassessmentsession.md)
  A session that your app uses to protect an assessment.
### Errors
- [struct AEAssessmentError](aeassessmenterror.md)
  Errors issued by an assessment session to its delegate.
- [AEAssessmentError.Code](aeassessmenterror/code.md)
  Error codes that the framework returns if a session fails.
- [let AEAssessmentErrorDomain: String](aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration)*