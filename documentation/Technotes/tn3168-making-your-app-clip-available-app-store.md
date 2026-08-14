# TN3168: Making your App Clip available in the App Store

**Framework**: Technotes

Learn how to configure your App Clip to prevent it from being unavailable in the App Store.

#### Overview

An App Clip is a lightweight version of your app that lets people quickly start and finish a task from your app, without downloading and installing it. People launch your App Clip by performing an invocation, for example, by scanning an App Clip Code at a physical location, tapping a link in the Maps app, or tapping an App Clip preview. To configure how your App Clip is launched, you create a [`default App Clip experience`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-a-default-app-clip-experience) and optional [`advanced App Clip experiences`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience) in App Store Connect. To learn how to configure, build, test, and distribute an App Clip, see [`App Clips`](https://developer.apple.com/documentation/appclip).

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

After you update your App Clip, create a release build of your app that includes it, then inspect the `.ipa` file of your app. Confirm that the bundle ID in the `Info.plist` file of your released App Clip matches your registered bundle ID. To inspect an `.ipa` file, follow the instructions in [`Doing basic optimization to reduce your app’s size`](https://developer.apple.com/documentation/xcode/doing-basic-optimization-to-reduce-your-app-s-size). To learn how to create a release build of your app, see [`Testing a release build`](https://developer.apple.com/documentation/xcode/testing-a-release-build).

#### Set Up Your Advanced App Clip Experience with an Approved Place Association

To create an advanced app Clip experience that appears in Apple Maps, you define a place association that connects the App Clip experience to a physical location in App Store Connect. Set the place association to a location approved for your business on Apple Maps. For more information, see [`advanced App Clip experiences`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience).

#### Avoid Using the Enterprise Distribution Method

Enterprise distribution isn’t available to App Clips. To distribute your App Clip to registered devices, use the Ad Hoc or Development method. To distribute an app that includes your App Clip to testers or on the App Store, use the App Store method. For more information about available distribution options, see [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).

#### Cache Your App Clip Before Testing Your Local Experience

To test your App Clip with a local experience, build your App Clip, sign it for Development, Ad Hoc, or TestFlight distribution, then run your App Clip on your test device to cache it. Local experiences don’t launch an App Clip that’s published on the App Store. For more information, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip).

#### Clear the Cache Before Testing Your Advanced App Clip Experiences

To show new or updated App Clip experiences, clear the cache on your device before performing invocations for your advanced App Clip experiences. For more information, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip).

#### Retry Your Invocation Later

In rare cases, your App Clip may become unavailable due to factors outside of your control. After Apple approves your App Clip, it may unexpectedly take some time for your App Clip to be available in all the countries or regions you select in App Store Connect. The same situation may occur when you edit your App Clip information in App Store Connect. Retry your invocation at a later time.

#### Revision History

- **2024-06-04** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3168-making-your-app-clip-available-app-store)*