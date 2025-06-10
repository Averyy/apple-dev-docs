# Explore more content with MusicKit

**Framework**: MusicKit

Track your outdoor runs with access to the Apple Music catalog, personal recommendations, and your own personal music library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Xcode 14.0+

#### Overview

> **Note**: This sample code project is associated with WWDC22 session [`110347: Explore more content with MusicKit`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110347/).

##### 4042109

This sample code project doesn’t work in the simulator. Before you run the sample code project in Xcode, perform the following steps:

1. In Xcode’s Project navigator, select the project, and click the Signing & Capabilities tab.
2. From the Team pop-up menu, choose your developer team.
3. In the Bundle Identifier field, enter a new bundle ID for the MusicMarathon target. The bundle identifier for the project has an associated App ID, so you need a unique identifier to create your own App ID. Use a reverse-DNS format for your identifier, as [`Preparing your app for distribution`](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution) describes.
4. In Safari, visit the [`Certificates, Identifiers, and Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) section of the Apple Developer website.
5. Select Identifiers, and click the Add button to create a new App ID for `MusicMarathon`. Follow the steps until you reach the Register an App ID page.
6. For the Bundle ID, select Explicit, and enter the bundle ID from step 2.
7. Click the App Services tab, and select the MusicKit checkbox.
8. Complete the App ID creation process.

After creating your App ID, your Xcode project needs no additional configuration. The MusicKit app service is a runtime service that automatically associates with your app’s bundle ID.

## See Also

- [Using Automatic Developer Token Generation for Apple Music API](using-automatic-token-generation-for-apple-music-api.md)
  Enable your app’s integration with the MusicKit App Service in the developer portal.
- [Using MusicKit to Integrate with Apple Music](using_musickit_to_integrate_with_apple_music.md)
  Find an album in Apple Music that corresponds to a CD in a user’s collection, and present the information for the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/explore_more_content_with_musickit)*