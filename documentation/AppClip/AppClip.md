# App Clips

**Framework**: App Clips  
**Kind**: module

Create a lightweight, in-the-moment experience or demo version for your app that’s instantly available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Overview

An  is a lightweight version of your app that offers access to some of the app’s functionality. For example, a donut shop’s app a person downloads and installs from the App Store may allow them to order donuts, save favorites, collect rewards, get special offers, and so on. The donut shop’s App Clip is instantly available – for example, when someone searches for “donuts” near the shop – without the need to install the full app. To ensure a fast launch experience and a fast order experience, the App Clip offers only the functionality to order donuts.

![A flowchart illustrating the flow for an App Clip. From left to right, the images shows an App Clip Code as an invocation, an App Clip card for a food truck, the App Clip of the food truck, and a donut.](https://docs-assets.developer.apple.com/published/2975a51a17a489e70989a1950106630c/app-clips-invocation-overview%402x.png)

App Clips that conform to a set of constraints can be larger in size, making it possible to offer an App Clip that’s a demo version of your app. The larger demo size allows people to experience your app’s functionality without a purchase or subscription. For example, a game might offer an App Clip to play the first level, a fitness app might offer an App Clip with a free workout, and so on. When a person has finished the game’s first level or completed the free workout, the App Clip displays a prompt to install the full app.

##### Offer a Great User Experience

App Clips provide a polished user experience that helps users solve a real-world task as quickly as possible or effortlessly try out a new app. Additionally, App Clips don’t appear on the Home screen, and users don’t manage them the way they manage full apps. Instead, the system removes an App Clip from a device after a period of inactivity, emphasizing the importance of a polished user experience.

For design guidance, see [`Human Interface Guidelines > App Clips`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/).

##### Review App Clip Creation

Limit the function of an App Clip to ensure a fast launch experience, protect user privacy, and preserve resources for in-the-moment experiences and demo versions of your app. Before you create an App Clip:

1. Review technology available to App Clips and constraints that ensure a good user experience.
2. Identify which of your app’s functionalities might make a great App Clip.
3. Learn how people discover and launch App Clips with  and how you configure App Clip experiences and use invocation URLs to offer a great launch experience.

For more information, refer to [`Choosing the right functionality for your App Clip`](choosing-the-right-functionality-for-your-app-clip.md) and [`Configuring App Clip experiences`](configuring-the-launch-experience-of-your-app-clip.md).

When you’ve identified functionality for your App Clip and identified invocations:

- Make changes to your app’s Xcode project and your code; for example, add an App Clip target and share code between your App Clip and full app.
- Add code to respond to invocations and to handle invocation URLs.
- Create App Clip experiences in App Store Connect.
- Optionally, associate your App Clip with your website to support additional invocations and advanced App Clip experiences.
- Optionally, create App Clip Codes that offer the best experience for people to discover and launch your App Clip.

## Topics

### Essentials
- [Choosing the right functionality for your App Clip](choosing-the-right-functionality-for-your-app-clip.md)
  Review frameworks available to App Clips and identify functionality that makes a great App Clip.
- [Configuring App Clip experiences](configuring-the-launch-experience-of-your-app-clip.md)
  Review how people launch your App Clip with invocation URLs, default and demo links, and advanced App Clip experiences.
- [App Clips updates](../Updates/AppClips.md)
  Learn about important changes in App Clips.
### Creation
- [Creating an App Clip with Xcode](creating-an-app-clip-with-xcode.md)
  Add an App Clip target to your Xcode project and share code between the App Clip and its corresponding full app.
- [Fruta: Building a feature-rich app with SwiftUI](fruta-building-a-feature-rich-app-with-swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Parent Application Identifiers Entitlement](../BundleResources/Entitlements/com.apple.developer.parent-application-identifiers.md)
  A list of parent application identifiers for an App Clip with exactly one entry.
- [com.apple.developer.associated-appclip-app-identifiers](../BundleResources/Entitlements/com.apple.developer.associated-appclip-app-identifiers.md)
  A list of App Clip identifiers for an app with exactly one entry.
- [com.apple.developer.on-demand-install-capable](../BundleResources/Entitlements/com.apple.developer.on-demand-install-capable.md)
  A Boolean value that indicates whether a bundle represents an App Clip.
### Launch
- [Responding to invocations](responding-to-invocations.md)
  Add code to respond to invocations and offer a focused launch experience.
- [Associating your App Clip with your website](associating-your-app-clip-with-your-website.md)
  Enable the system to verify your App Clip to support invocations from your website and devices running iOS 16.3 or earlier.
- [Supporting invocations from your website and the Messages app](supporting-invocations-from-your-website-and-the-messages-app.md)
  Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.
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
- [Encoding a URL in an App Clip Code](encoding-a-url-in-an-app-clip-code.md)
  Choose an invocation URL for your App Clip Code that you can encode efficiently.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppClip)*