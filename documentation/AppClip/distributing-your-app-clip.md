# Distributing your App Clip

**Framework**: App Clips

Archive the full app for your App Clip, upload it to App Store Connect, and distribute it to testers or publish it on the App Store.

#### Overview

When you submit an App Clip for distribution to testers with [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/) or for publishing in the App Store, you don’t submit the App Clip on its own; you export and submit the app bundle of the full app that includes the App Clip.

> **Note**:  You may also choose Ad Hoc or Development distribution. Note that you need to export the App Clip and the full app separately in these cases. Enterprise distribution isn’t available to App Clips.

 You may also choose Ad Hoc or Development distribution. Note that you need to export the App Clip and the full app separately in these cases. Enterprise distribution isn’t available to App Clips.

##### Archive Your App and Upload It to App Store Connect

Uploading an app archive that contains the full app and the App Clip works just like for an app that doesn’t come with an App Clip. To export an App Clip for distribution to testers:

1. In Xcode, archive the App Clip’s corresponding app, open the Organizer window, select the archive, and click Distribute App.
2. Choose App Store Connect as the distribution method, then upload the app.
3. To distribute the app that features an App Clip to testers with [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/) or publish it on the App Store, visit [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/login).

![Screenshot showing the sheet for choosing the distribution method; App Store Connect is selected.](https://docs-assets.developer.apple.com/published/be6cf7baabaff8af99d82917df0ca91f/media-3678139%402x.png)

For additional information, see [`Testing the launch experience of your App Clip`](testing-the-launch-experience-of-your-app-clip.md) and [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/distributing-your-app-clip)*