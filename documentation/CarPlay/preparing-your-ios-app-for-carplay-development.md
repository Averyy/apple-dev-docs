# Preparing your iOS app for CarPlay development

**Framework**: CarPlay  
**Role**: Article

Configure the entitlements and provisioning profile you need to run your iOS app in CarPlay environments.

## Overview

A CarPlay app is part of your existing iOS app, and you use it to offer your content in a person’s vehicle or in Apple HomeView. Adding CarPlay support is a good option for many types of iOS apps, but not all. For example, CarPlay doesn’t support games or apps that might distract someone while driving. To ensure apps offer only relevant features, Apple requires apps to have entitlements for the features they support. If an app doesn’t have a supported CarPlay entitlement, the system doesn’t show the app in CarPlay environment.

Before you begin developing a CarPlay version of your app, review the supported app types to determine if one of them aligns with your app’s content. If adding CarPlay support to your app makes sense, request the associated entitlement from Apple early in your development process. While you wait for Apple to approve your request, you can start adding CarPlay features to your app and continue to build the iOS version of your app. However, you can’t your app in a CarPlay environment until you have the requested entitlement, and add it to the App ID and provisioning profile for your app.

> ❗ **Important**: During the implementation of your CarPlay app, adhere to the required guidelines for the type of app you create. For the list of App Store Review guidelines specific to CarPlay apps, see the [CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf).

For the list of supported app types, see [CarPlay app types](./CarPlay.md#CarPlay-app-types).

## Request a CarPlay entitlement for your app

CarPlay supports many different types of apps, and each app type requires a specific entitlement. Before you develop your CarPlay app, request the entitlement that matches the features your app offers:

1. Navigate to [https://developer.apple.com/contact/carplay](https://developer.apple.com/contact/carplay).
2. Provide information about your organization.
3. Select the type of app you’re planning to create.
4. Agree to the Terms and Conditions.

Apple reviews each application using predefined criteria. If your request meets the criteria, Apple adds the entitlement to your developer account. You can then add the entitlement to your App ID and generate a provisioning profile for your Xcode project.

## Add the CarPlay capability to your App ID

After you receive CarPlay entitlements from Apple, add the entitlement to the App ID for your iOS app. CarPlay entitlements show up as capabilities in your developer account, and you can add them to any app that offers the relevant features. If you’re creating a new app, add the CarPlay capability at creation time. To edit an existing App ID:

1. Sign in to your [Apple Developer](https://developer.apple.com/account/) account and navigate to the Certificates, Identifiers & Profiles page.
2. Select Identifiers from the menu on the left.
3. Select the App ID for your app.
4. Select the Capabilities tab.
5. Enable the CarPlay capability your app requires.
6. Click the Save button.

![A screenshot showing the Edit your App ID Configuration page in the developer portal. The Additional Capabilities tab is in a selected state and lists the available CarPlay capabilities. The CarPlay Audio App for the CarPlay framework capability is in an enabled state.](https://developer.apple.com/tutorials/images/com.apple.carplay/media-3703055@2x.png)

For information on how to create a new App ID, see [Register an App ID](https://help.apple.com/developer-account/#/dev1b35d6f83).

## Generate a provisioning profile for your app

Adding support for CarPlay requires you to specify your app’s provisioning profile manually, instead of letting Xcode manage signing automatically. To generate the provisioning profile for your app:

1. Sign in to your [Apple Developer](https://developer.apple.com/account/) account.
2. Navigate to the Certificates, Identifiers & Profiles page.
3. Select Profiles from the menu on the left.
4. Click the plus (+) button to add a new profile.
5. Configure the profile with the App ID that contains your CarPlay entitlement.
6. Configure the rest of the provisioning profile with your team-specific details.
7. Generate the profile.

When you generate the provisioning profile, the developer site gives you the option to download it to your system. You can download the file if you want to manage it locally, but Xcode also gives you the option to download a provisioning profile when you select it for your project.

## Update your app’s signing and capabilities settings

The provisioning profile you generate for your app contains information Xcode needs to sign your iOS app after a build. To build a CarPlay app, you need to specify the provisioning profile manually. You also need to add an Xcode capability for the type of CarPlay app you’re creating:

1. In Xcode, select your project in the Project navigator.
2. Select your iOS app target.
3. Select the Signing & Capabilities tab.
4. Click All in the scope bar, and then deselect “Automatically manage signing”.
5. Click the Provisioning Profile pop-up menu and choose Download Profile. Xcode displays
6. Select your CarPlay provisioning profile from the list of available profiles and click Select Profile.
7. Back in the Signing & Capabilities tab, click the `+ Capability` button to add a new capability.
8. Select the CarPlay capability your app supports.

When you add a CarPlay capability, Xcode automatically creates or updates the entitlements file for your app. For example, if you add the CarPlay Audio app capability to your project, Xcode adds the `com.apple.developer.carplay-audio` key to the entitlements file. Xcode also displays the capability in the Signing & Capabilities tab. During signing, Xcode verifies that the CarPlay entitlement for the requested capability matches the entitlement in your app’s provisioning profile.

## Troubleshoot signing and app installation issues

After you install the updated provisioning profile and create your CarPlay app’s initial interface, you can build your app in Xcode, sign it, install it on a connected iPhone, and open CarPlay Simulator. If you configured your app correctly, CarPlay Simulator displays it on the Home Screen. However, if entitlements are missing or don’t match, issues can occur:

- If your app’s entitlements file and provisioning profile don’t refer to the same CarPlay app type, Xcode reports a signing error at build time.
- If your project uses automatic signing, instead of a custom provisioning profile, iOS doesn’t install the app in CarPlay.
- If your project’s entitlements file is missing, iOS doesn’t install the app in CarPlay.
- If you don’t run your iOS app on a connected iPhone, iOS doesn’t install the app in CarPlay.
- If you select a CarPlay Simulator configuration without the features your app requires, the simulator doesn’t show your app. For example, a video app requires a configuration that supports video playback.

After you verify the entitlements and provisioning profile are correct, try rebuilding your app with the CarPlay Simulator window open if your app still doesn’t appear. Even if CarPlay Simulator installs your app, the app can’t run without an initial scene. If an app supports the Now Playing template, the system can display it if no other scene is available. For all other types of apps, provide a scene and the root template for your interface.

For information on how to create your CarPlay app’s initial interface, see [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md). For information on how to run your app in CarPlay Simulator, see [Testing your app in CarPlay Simulator](./testing-your-app-in-carplay-simulator.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/preparing-your-ios-app-for-carplay-development)*