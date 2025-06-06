# TN3168: Making your App Clip available in the App Store

**Framework**: Technotes

Learn how to configure your App Clip to prevent it from being unavailable in the App Store.

#### Overview

An App Clip is a lightweight version of your app that lets people quickly start and finish a task from your app, without downloading and installing it. People launch your App Clip by performing an invocation, for example, by scanning an App Clip Code at a physical location, tapping a link in the Maps app, or tapping an App Clip preview. To configure how your App Clip is launched, you create a [`default App Clip experience`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-a-default-app-clip-experience) and optional [`advanced App Clip experiences`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience) in App Store Connect. To learn how to configure, build, test, and distribute an App Clip, see [`App Clips`](https://developer.apple.com/documentation/AppClip).

When you launch a debug or release build of your App Clip, you may discover that your App Clip fails to launch with the following error message:

```shell
This app clip is not currently available in your country or region
```

This error can occur in the following scenarios:

- The device has connectivity issues.
- The app is unavailable in the storefront associated with the Apple ID currently logged into the device.
- The App Clip uses unexpected configurations.

If your device has connectivity issues, wait until your network conditions improve to launch your App Clip again.

A customer’s [`Apple ID`](https://developer.apple.comhttps://developer.apple.com/help/glossary/apple-id) country or region determines the App Store country or region where they can purchase or download apps. For example, an Apple ID set to France can only purchase apps from the App Store in France. In App Store Connect, you can select the countries or regions where your app is available on the App Store. For more information, see [`Manage availability for your app on the AppStore`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app). Your App Clip is available anywhere your app is on the App Store. Before launching your App Clip on a device, confirm that your app is available in the country or region associated with the Apple ID currently logged into the device. For example, if your app is available in all countries or regions of the App Store except France, launching your App Clip on a device with an Apple ID set to France will fail with the above message.

Once you have a stable network and set up your app’s availability in App Store Connect, log in to your device with an Apple ID set to a country or region where your app is available, then perform an invocation. If your App Clip still fails to launch with the above message, review this document to find out how you can properly configure your App Clip for testing and App Store distribution.

#### Use a Bundle Id Registered in App Store Connect

You register a bundle ID for your App Clip when you upload the first build of your app that contains an App Clip to App Store Connect. You can’t change it after uploading your first build. Use this bundle ID anywhere you need to identify your App Clip, for example, when you change the bundle identifier field in the General pane of your App Clip’s target in Xcode or when you define a default App Clip link for your local App Clip experience.

After you update your App Clip, create a release build of your app that includes it, then inspect the `.ipa` file of your app. Confirm that the bundle ID in the `Info.plist` file of your released App Clip matches your registered bundle ID. To inspect an `.ipa` file, follow the instructions in [`Doing basic optimization to reduce your app’s size`](https://developer.apple.com/documentation/Xcode/doing-basic-optimization-to-reduce-your-app-s-size). To learn how to create a release build of your app, see [`Testing a release build`](https://developer.apple.com/documentation/Xcode/testing-a-release-build).

#### Set Up Your Advanced App Clip Experience with an Approved Place Association

To create an advanced app Clip experience that appears in Apple Maps, you define a place association that connects the App Clip experience to a physical location in App Store Connect. Set the place association to a location approved for your business on Apple Maps. For more information, see [`advanced App Clip experiences`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience).

#### Avoid Using the Enterprise Distribution Method

Enterprise distribution isn’t available to App Clips. To distribute your App Clip to registered devices, use the Ad Hoc or Development method. To distribute an app that includes your App Clip to testers or on the App Store, use the App Store method. For more information about available distribution options, see [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases).

#### Cache Your App Clip Before Testing Your Local Experience

To test your App Clip with a local experience, build your App Clip, sign it for Development, Ad Hoc, or TestFlight distribution, then run your App Clip on your test device to cache it. Local experiences don’t launch an App Clip that’s published on the App Store. For more information, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/AppClip/testing-the-launch-experience-of-your-app-clip).

#### Clear the Cache Before Testing Your Advanced App Clip Experiences

To show new or updated App Clip experiences, clear the cache on your device before performing invocations for your advanced App Clip experiences. For more information, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/AppClip/testing-the-launch-experience-of-your-app-clip).

#### Retry Your Invocation Later

In rare cases, your App Clip may become unavailable due to factors outside of your control. After Apple approves your App Clip, it may unexpectedly take some time for your App Clip to be available in all the countries or regions you select in App Store Connect. The same situation may occur when you edit your App Clip information in App Store Connect. Retry your invocation at a later time.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3168-making-your-app-clip-available-app-store)*