# Preparing your app to be the default messaging app

**Framework**: Messages

Configure your messaging app so people can set it as the default on their device.

#### Overview

In iOS and iPadOS 18.2 and later, a person may select an app other than the Messages app to send instant messages. If your app provides messaging services and you wish to optionally become the default messaging app, there are several steps you need to take.

##### Add the Default Messaging App Entitlement to Your Project

Add the `com.apple.developer.messaging-app` entitlement to the `.entitlements` file in your app’s Xcode project. For instructions on how to add this entitlement, see [`Default Messaging App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.messaging-app).

##### Add the Instant Messaging Im Url Type Support and Url Scheme to Your Apps Infoplist and Xcode Project

Add the `im:` support to your app’s `Info.plist` file, following these steps:

1. In your app’s Xcode project, select the `Info.plist` file in the File Navigator.
2. Open the URL Types array (or add the array, if necessary, by creating a new entry and selecting URL Types from the dropdown menu).
3. Add a new URL scheme to the URL Types array, and set its string value to `im`.

Next, in order for your app to open incoming `im:` URLs, it needs to support this as a custom URL scheme.

To add this support, see [`Defining a custom URL scheme for your app`](https://developer.apple.com/documentation/Xcode/defining-a-custom-url-scheme-for-your-app).

##### Process Incoming Messaging Urls in Your App

> **Note**: The `im:` URL scheme format is identical to the `sms:` URL scheme format, which is `im:NUMBER` or `sms:NUMBER`, respectively. To use an email address, use `im:EMAIL` or `sms:EMAIL`. The `NUMBER` URL string can contain the digits 0 through 9, the plus (+), hyphen (-), and period (.) characters. The URL string must not include any message text or other information.

You can process incoming messages using either [`scene(_:openURLContexts:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:openURLContexts:)) delegate method or the `UIApplication` delegate method [`application(_:open:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:options:)).

##### Provide Fallback Behavior in Your App

In cases where your app can’t handle the provided phone number, you can configure a fall back to the system to deliver with the Messages app, if it’s installed. Your app can do this by reformatting the incoming `im:` URL to a `sms:` URL, then forwarding it using the [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/open(_:options:completionHandler:)) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/preparing-your-app-to-be-the-default-messaging-app)*