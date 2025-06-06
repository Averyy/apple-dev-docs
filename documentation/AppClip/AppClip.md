# App Clips

**Framework**: Appclip  
**Kind**: module

Provide people a shortcut to selected content and features of your app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

#### Overview

An  is a lightweight version of your app that offers people access to some of the app’s functionality. A coffee shop app downloaded and installed from the App Store, for example, might provide people the ability to order a drink, save favorites, collect rewards, get special offers, and so on. The coffee shop App Clip only offers the functionality to order a drink.

![A flowchart illustrating the flow for an App Clip. From left to right, the images shows an App Clip Code as an invocation, an App Clip card for a donut shop, the App Clip of the donut shop, and a donut.](https://docs-assets.developer.apple.com/published/1fa269ccc94c2866e6b1c27d127a4cb5/media-4301753%402x.png)

People find an App Clip by performing an  for example, by tapping a location-based suggestion from Siri Suggestions or by scanning an App Clip Code. After a person confirms the invocation, the App Clip launches instantly, helps a person perform an everyday task as quickly as possible, and only stays on their device for as long as they need it. When a person installs the corresponding full app for your App Clip, the full app replaces the App Clip. From this moment on, confirming an invocation launches the full app instead of the App Clip, and a person gets the functionality of the App Clip within the full app. If they don’t install the full app, the system automatically removes the App Clip after a period of inactivity.

Again, consider the coffee shop’s App Clip: When a person walks past the coffee shop, the system displays a location-based suggestion from Siri Suggestions on their device. They tap the suggestion, confirm the launch of the App Clip on the system-provided , and instantly use the App Clip to order a drink. After a person completes the order, the App Clip recommends its corresponding app to them, and they download the app. The next time they tap the location-based suggestion, they launch the full app instead of the App Clip. If they don’t install the app, tapping the suggestion and confirming the invocation continues launching the App Clip.

> **Note**:  Session 10178: [`What’s new in App Clips`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10178) (WWDC23) Session 10097: [`What’s new in App Clips`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10097) (WWDC22) Session 10013: [`Build light and fast App Clips`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10013) (WWDC21) Session 10012:  [`What’s new in App Clips`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10012) (WWDC21)

##### Offer a Great User Experience

App Clips provide a polished user experience that helps users solve a real-world task as quickly as possible. Additionally, App Clips don’t appear on the Home screen, and users don’t manage them the way they manage full apps. Instead, the system removes an App Clip from a device after a period of inactivity, emphasizing the importance of a polished user experience.

For design guidance, see [`Human Interface Guidelines > App Clips`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/).

##### Review App Clip Creation

Limit the function of an App Clip to ensure a fast launch experience, protect user privacy, and preserve resources. Before you create an App Clip, first review the technology available to App Clips and identify which of your app’s functionalities would make a great App Clip. When you create an App Clip, plan to spend time with:

- Making changes to your app’s Xcode project and your code, for example, adding an App Clip target or sharing code between your App Clip and full app
- Planning the launch experience for your App Clip, identifying invocations to support, and adding code to respond to them
- Associating your App Clip with your website to support additional invocations and advanced App Clip experiences (optional)
- Creating App Clip experiences in App Store Connect
- Creating App Clip Codes that offer the best experience for people to discover and launch your App Clip (optional)

## Topics

### Essentials
- [Choosing the right functionality for your App Clip](choosing-the-right-functionality-for-your-app-clip.md)
  Review frameworks available to App Clips and identify functionality that makes a great App Clip.
### Creation
- [Creating an App Clip with Xcode](creating-an-app-clip-with-xcode.md)
  Add an App Clip target to your Xcode project and share code between the App Clip and its corresponding full app.
- [Fruta: Building a Feature-Rich App with SwiftUI](fruta_building_a_feature-rich_app_with_swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Parent Application Identifiers Entitlement](../BundleResources/Entitlements/com.apple.developer.parent-application-identifiers.md)
  A list of parent application identifiers for an App Clip with exactly one entry.
- [com.apple.developer.associated-appclip-app-identifiers](../BundleResources/Entitlements/com.apple.developer.associated-appclip-app-identifiers.md)
  A list of App Clip identifiers for an app with exactly one entry.
- [com.apple.developer.on-demand-install-capable](../BundleResources/Entitlements/com.apple.developer.on-demand-install-capable.md)
  A Boolean value that indicates whether a bundle represents an App Clip.
### Launch
- [Configuring the launch experience of your App Clip](configuring-the-launch-experience-of-your-app-clip.md)
  Review how people launch your App Clip, identify invocation URLs, make use of default App Clip links, and configure experiences in App Store Connect.
- [Associating your App Clip with your website](associating-your-app-clip-with-your-website.md)
  Enable the system to verify your App Clip to support invocations in iOS 16.3 or earlier and from your website.
- [Supporting invocations from your website and the Messages app](supporting-invocations-from-your-website-and-the-messages-app.md)
  Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.
- [Responding to invocations](responding-to-invocations.md)
  Add code to respond to invocations and offer a focused launch experience.
- [Confirming a person’s physical location](confirming-a-person-s-physical-location.md)
  Add code to quickly confirm a person’s physical location while respecting their privacy.
- [Launching another app’s App Clip from your app](launching-another-app-s-app-clip-from-your-app.md)
  Enable people to launch another app’s App Clip from your app with App Clip links and offer a rich preview of it with the Link Presentation framework.
- [class APActivationPayload](apactivationpayload.md)
  Information that’s passed to an App Clip on launch.
- [NSAppClip](../BundleResources/Information-Property-List/NSAppClip.md)
  A collection of keys that an App Clip uses to get additional capabilities.
### App Clip Codes
- [Creating App Clip Codes](creating-app-clip-codes.md)
  Help users discover your App Clip by using an NFC-integrated or scan-only App Clip Code.
- [Preparing multiple App Clip Codes for production](preparing-multiple-app-clip-codes-for-production.md)
  Prepare your App Clip Codes to send to a professional printing service.
- [Interacting with App Clip Codes in AR](interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
### App Clip to full app transition
- [Recommending your app to App Clip users](recommending-your-app-to-app-clip-users.md)
  Display an overlay in your App Clip to recommend your app to users.
- [Sharing data between your App Clip and your full app](sharing-data-between-your-app-clip-and-your-full-app.md)
  Use CloudKit, Sign in with Apple, shared user defaults or containers, and the keychain to offer a smooth transition from your App Clip to your app.
### Notifications
- [Enabling notifications in App Clips](enabling-notifications-in-app-clips.md)
  Enable your App Clip to schedule and receive notifications for a short or extended time period.
### Live Activities
- [Offering Live Activities with your App Clip](offering-live-activities-with-your-app-clip.md)
  Add a widget extension to your App Clip target and use ActivityKit to display Live Activities on the Lock Screen and in the Dynamic Island.
### Testing
- [Testing the launch experience of your App Clip](testing-the-launch-experience-of-your-app-clip.md)
  Debug App Clip invocations, test the launch experience, and verify the configuration of your released App Clip.
### Distribution
- [Distributing your App Clip](distributing-your-app-clip.md)
  Archive the full app for your App Clip, upload it to App Store Connect, and distribute it to testers or publish it on the App Store.
### Articles
- [Creating App Clip Codes with App Store Connect](creating-app-clip-codes-with-app-store-connect.md)
  Select one or more advanced App Clip experiences in App Store Connect and create App Clip Codes for users to scan to launch your App Clip.
- [Creating App Clip Codes with the App Clip Code Generator](creating-app-clip-codes-with-the-app-clip-code-generator.md)
  Use the App Clip Code Generator command-line tool to verify your code’s colors, get color suggestions, and create App Clip Codes.
- [Encoding a URL in an App Clip Code](encoding-a-url-in-an-app-clip-code.md)
  Choose an invocation URL for your App Clip Code that you can encode efficiently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppClip)*