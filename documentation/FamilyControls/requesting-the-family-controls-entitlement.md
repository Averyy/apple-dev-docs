# Requesting the Family Controls entitlement

**Framework**: FamilyControls

Register your app and its Screen Time API app extensions to use Family Controls.

#### Overview

Before you distribute an app that uses Family Controls, your Apple Developer Account Holder must request permission to use the [`Family Controls`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement, and update your Xcode project to use the entitlement.

##### Request the Entitlement

Request the Family Controls entitlement at [`Family Controls distribution`](https://developer.apple.comhttps://developer.apple.com/contact/request/family-controls-distribution). If your app includes a Screen Time API app extension such as Device Activity Monitor, Device Activity Report, Shield Action, or Shield Configuration, submit the same request for the extension. For more information on the Screen Time APIs, see [`Screen Time Technology Frameworks`](https://developer.apple.comhttps://developer.apple.com/documentation/ScreenTimeAPIDocumentation).

> **Note**: You can also use the [`Capability Requests`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/capability-requests/) tab in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/) to request permission to use the Family Controls entitlement for distribution. For more information, see [`Capability Requests`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/capability-requests/).

Apple reviews your app, and if it’s approved, adds the entitlement to your developer account using managed capabilities. For more information, see [`Provisioning with capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities).

##### Check the Status of Your Request

To check your request status, follow the steps in Check the status of your request in [`Capability Requests`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/capability-requests/), then select Family Controls from the Capabilities list. When Apple approves your request, [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/) displays an Assigned status for this capability.

![A Capability Requests tab showing Family Controls (Distribution) capability with Assigned status and a search field containing Family Controls.](https://docs-assets.developer.apple.com/published/9a56159ed272a6b14b725f3dfb03ec0b/family-controls-assigned%402x.png)

Click the info button next to the capability. In the dialog that appears, check that Provisioning Support lists all the distribution methods you need.

![A Capability Requests tab for Family Controls showing the entitlement key com.apple.developer.family-controls and distribution capability with Assigned status.](https://docs-assets.developer.apple.com/published/e829b8bd60a36777a6169b69a5ce0f47/family-controls-support%402x.png)

##### Configure the Family Controls Entitlement for Your App

When you receive the Family Controls entitlement, update your Xcode project to use it. For more information, see [`Configuring Family Controls`](https://developer.apple.com/documentation/Xcode/configuring-family-controls).

If your Xcode project already includes the Family Controls capability for development and you use automatic signing, Xcode automatically updates your app to use this capability for distribution.

## See Also

- [class AuthorizationCenter](authorizationcenter.md)
  The center for requesting authorization to provide parental controls.
- [enum AuthorizationStatus](authorizationstatus.md)
  The status of your app’s authorization to provide parental controls.
- [Family Controls](../BundleResources/Entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement)*