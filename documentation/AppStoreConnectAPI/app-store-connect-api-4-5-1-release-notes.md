# App Store Connect API 4.5.1 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.5.1 provides resources that enable you to automate actions you take in App Store Connect.

#### Added

- Manage your app’s marketing and product media from one place with the App Asset Library. Upload an image once with [`Create an app asset library image`](post-v1-appassetlibraryimages.md) or a video with [`Create an app asset library video`](post-v1-appassetlibraryvideos.md), read an app’s library with [`Read related asset library`](get-v1-apps-_id_-assetlibrary.md), and list its assets through [`List related images`](get-v1-appassetlibraries-_id_-images.md) and [`List related videos`](get-v1-appassetlibraries-_id_-videos.md). For more information, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).
- Reuse library assets across App Store surfaces. Use [`Create an app asset library placement`](post-v1-appassetlibraryplacements.md) to place an image or video on an App Store version localization, custom product page localization, in-app event localization, or App Store version experiment treatment localization, and [`Create an app asset library placement ordering request`](post-v1-appassetlibraryplacementorderingrequests.md) to set the order in which placements appear. Read the placements for a localization through [`List related placements`](get-v1-appstoreversionlocalizations-_id_-placements.md), [`List related placements`](get-v1-appcustomproductpagelocalizations-_id_-placements.md), [`List related placements`](get-v1-appeventlocalizations-_id_-placements.md), and [`List related placements`](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-placements.md).
- Discover valid asset specifications instead of hard-coding them. Use [`List app asset library ref data`](get-v1-appassetlibraryrefdata.md) to read the supported placement types, dimensions, and limits for the library.
- Target iPhone Duo screenshots and app previews with the new `IPHONE_DUO` display class in [`AppAssetLibraryDisplayClass`](appassetlibrarydisplayclass.md). Use [`List app asset library ref data`](get-v1-appassetlibraryrefdata.md) to read its placement groups and screen dimensions.

#### Deprecated

- The [`App Screenshot Sets`](app-screenshot-sets.md), [`App Screenshots`](app-screenshots.md), [`App Preview Sets`](app-preview-sets.md), and [`App Previews`](app-previews.md) resources are deprecated. Manage App Store version, custom product page, and experiment treatment media with [`App Asset Library images`](app-asset-library-images.md), [`App Asset Library videos`](app-asset-library-videos.md), and [`App Asset Library placements`](app-asset-library-placements.md) instead.
- The [`App Event Screenshots`](app-event-screenshots.md) and [`App Event Video Clips`](app-event-video-clips.md) resources are deprecated. Manage in-app event media with [`App Asset Library images`](app-asset-library-images.md), [`App Asset Library videos`](app-asset-library-videos.md), and [`App Asset Library placements`](app-asset-library-placements.md) instead.
- To move an existing integration, see [`Migrating to the App Asset Library`](migrating-to-the-app-asset-library.md).

## See Also

- [App Store Connect API 4.5 release notes](app-store-connect-api-4-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.4 release notes](app-store-connect-api-4-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3.1 release notes](app-store-connect-api-4-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.4 release notes](app-store-connect-api-3-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-5-1-release-notes)*