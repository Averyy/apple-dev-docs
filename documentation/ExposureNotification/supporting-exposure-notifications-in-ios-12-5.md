# Supporting Exposure Notifications in iOS 12.5

**Framework**: Exposure Notification

Prepare your Exposure Notifications app to run on a previous version of iOS.

#### Overview

To increase adoption and broaden usage, the Exposure Notification framework now supports iPhones compatible with iOS 12.5. Because Exposure Notifications was originally released in iOS 13.5, special considerations apply when developing for iOS 12.5. However, all privacy protections put in place with the original release also apply in iOS 12.5.

##### Determine the Level of Support You Need

Depending on your circumstances, you have a couple of options for adopting Exposure Notifications.

If you havenʼt already developed an Exposure Notifications app, or if you have an existing app that uses features in later versions of iOS that arenʼt available in iOS 12.5, consider using Exposure Notifications Express, which provides an app-less experience. For more information, see [`Supporting Exposure Notifications Express`](supporting-exposure-notifications-express.md).

If you have an app that uses version 1 risk scoring and want to support iOS 12.5, consider updating to the more robust version 2 scoring. For more information, see [`ENExposureConfiguration`](enexposureconfiguration.md).

##### Set the Deployment Target and Link the Framework

Exposure Notifications for iOS 12.5 requires Xcode 12.3 or later. In your Xcode project’s Build Settings tab, set the iOS deployment target. From the menu, select Other and type “12.5.”

![Image that shows iOS Deployment Target set to iOS 12.5.](https://docs-assets.developer.apple.com/published/4578d6ca8c268ce64a49ee239ed6a876/media-3705948%402x.png)

Select the Exposure Notification framework explicitly in the Link Binary With Libraries section under Build Phases. Set the status of the framework to Optional.

![Image that shows how to add the Exposure Notification framework to your Xcode project.](https://docs-assets.developer.apple.com/published/8ee1e8d23b2ff7db3f331d27f2f006d2/media-3705004%402x.png)

##### Perform Api and Ios Version Checks

Extend your app to handle different versions of iOS and Exposure Notifications by incorporating the following code. Call `getSupportedExposureNotificationsVersion()` to determine if Exposure Notifications is available on the device, and if so, which API version to support.

Although iOS 13.0 to 13.4 doesn’t support Exposure Notifications, your app might still download onto devices with those versions of iOS. If that happens, present a dialog to let the user know Exposure Notifications isn’t available for their device.

##### Set Background Task Interval and Request Runtime

Apps that support Exposure Notifications periodically need time in the background to download and evaluate temporary exposure keys. Because [`BGTaskScheduler`](https://developer.apple.com/documentation/BackgroundTasks/BGTaskScheduler) isn’t available in iOS 12.5, Bluetooth explicitly grants apps with the Exposure Notifications entitlement 3.5 minutes at least once a day.

Add the following code to your app to prepare it to receive background processing time at the defined interval.

Background scheduling starts when the user authorizes and enables Exposure Notifications for the app. Upon user authorization, the first iteration of the background launch happens after the defined interval, and after every subsequent interval. If the app loses authorization, scheduling stops immediately.

Add the following code to your app to extend the `setLaunchActivityHandler` to download and detect exposures.

## See Also

- [Supporting Exposure Notifications Express](supporting-exposure-notifications-express.md)
  Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](building-an-app-to-notify-users-of-covid-19-exposure.md)
  Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](setting-up-a-key-server.md)
  Ensure that your server meets the requirements for supporting Exposure Notifications.
- [class ENManager](enmanager.md)
  A class that manages exposure notifications.
- [ENDeveloperRegion](../BundleResources/Information-Property-List/ENDeveloperRegion.md)
  A string that specifies the region that the app supports.
- [ENAPIVersion](../BundleResources/Information-Property-List/ENAPIVersion.md)
  A number that specifies the version of the API to use.
- [Changing Configuration Values Using the Server‑to‑Server API](changing-configuration-values-using-the-server-to-server-api.md)
  Update Exposure Notifications configuration values from a Public Health Authority’s server.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](testing-exposure-notifications-apps-in-ios-13-7-and-later.md)
  Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-in-ios-12-5)*