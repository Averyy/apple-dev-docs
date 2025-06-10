# Preparing your app to be the default calling app

**Framework**: CallKit

Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.

#### Overview

In iOS and iPadOS 18.2 and later, a person may select an app other than the Phone app or FaceTime to handle calls. A calling app handles `tel:` URLs the system sends to it. For example, when someone selects your app as the default calling app, tapping on a telephone number in a contact card initiates an attempt to place the call using your app.

If your app places phone calls and you wish to optionally become the default calling app, there are several steps you need to take.

##### Add the Default Calling App Entitlement to Your Project

Add the `com.apple.developer.calling-app` entitlement to the `.entitlements` file in your app’s Xcode project. For instructions on how to add this entitlement, see [`Default Calling App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.calling-app).

##### Apply the Fallback Url Scheme in Your App

If starting a VoIP conversation fails, you may wish to have the conversation fall back to the system to handle it. While optional, providing a fallback gives people another opportunity to have the conversation. When you let the conversation fall back to the system, it handles the conversation as a cellular network conversation. To provide a fallback, adopt the `telephony:` URL scheme as the fallback handler for the  [`scene(_:continue:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:continue:)) delegate callback. For example:

```swift
    let handle = userActivity.startCallHandle // The `UserActivity` structure the system provides; the `startCallHandle` property is the phone number the system is passing to your app.
    var urlComponents = URLComponents()
    urlComponents.scheme = "telephony"
    urlComponents.path = handle  

    guard let url = urlComponents.url else { return } 

    UIApplication.shared.open(url)
```

> **Note**: Only use the `telephony:` URL scheme as a fallback behavior in response to a person’s explicit action in your app, such as clicking a call button after your app presents the proposed number to call.

For more information on VoIP calling related intents, see [`INStartCallIntent`](https://developer.apple.com/documentation/Intents/INStartCallIntent).

##### Prepare Your App for Submission to App Store Connect

To submit your app to App Store Connect, your app needs to meet the following criteria:

- The `com.apple.developer.calling-app` entitlement is in its `.entitlements` file, and it’s set to a value of `true`.
- The `Info.plist` file has the `UIBackgroundModes` property array and contains an entry with the string `voip`.
- Your app links to either the [`CallKit`](CallKit.md) or [`LiveCommunicationKit`](https://developer.apple.com/documentation/LiveCommunicationKit) frameworks.

> 💡 **Tip**: To add a `voip` entry in the `Info.plist` file’s `UIBackgroundModes` property array, select the “App provides Voice over IP services” option from the dropdown menu.

## See Also

- [class CXProvider](cxprovider.md)
  An object that represents a telephony provider.
- [protocol CXProviderDelegate](cxproviderdelegate.md)
  A collection of methods that a telephony provider object calls.
- [class CXProviderConfiguration](cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [CallKit updates](../Updates/CallKit.md)
  Learn about important changes to CallKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/preparing-your-app-to-be-the-default-calling-app)*