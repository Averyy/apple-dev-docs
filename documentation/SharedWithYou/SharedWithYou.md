# Shared With You

**Framework**: Sharedwithyou  
**Kind**: module

Surface shared content and collaborate in your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Mentions

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)

#### Overview

Access and view content shared from Messages across the system and continue the messaging experience without leaving your app. Incorporate Shared with You to make it easier for people to access content shared through conversations or notifications.

![An image of an iPhone. In the middle of the screen is a Shared with You shelf with three list items arranged vertically. Each list item has a gray rectangle with text next to it. All three rows have Title as the title and Subtitle as the subtitle. Below the subtitle in all three rows is an oval button with the title From Juan.](https://docs-assets.developer.apple.com/published/cbf165ab43e7dff75cbc6c588785e19f/media-4301694%402x.png)

Support a Shared with You shelf in your app to visually represent shared items with an [`SWAttributionView`](swattributionview.md) that the system renders. Securely share universal links that your app accesses using the [`SWHighlight`](swhighlight.md) class. For information on getting started, see [`Making your app content shareable`](making-your-app-content-shareable.md).

> **Note**:  Session 10094: [`Add Shared with You to your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10094)

## Topics

### Shared content
- [Making your app content shareable](making-your-app-content-shareable.md)
  Add support for universal links and a Shared with You shelf to support shared content in your app.
- [Shared content interactions](shared-content-interactions.md)
  Use highlights and attribution views to manage participants and trigger events for shared content.
### Collaboration
- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)
  Manage shared content collaboration in your app using CloudKit and iCloud Drive.
- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)
  Integrate your custom collaboration app with Messages.
- [Collaboration views](collaboration-views.md)
  Create and customize a collaboration view to manage the shared content actions.
### Framework versions
- [Version number](version-number.md)
- [Version string](version-string.md)
### Macros
- [Macros](macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SharedWithYou)*