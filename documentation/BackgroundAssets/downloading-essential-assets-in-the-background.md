# Downloading essential assets in the background

**Framework**: Backgroundassets

Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 18.4+
- visionOS 2.4+
- Xcode 15.0+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10108: [`What’s new in Background Assets`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10108/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

- Configure the WWDC Sessions and WWDC Sessions Background Assets Extension targets to use your Developer team for signing.
- See [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).

## See Also

- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BackgroundAssets/downloading-essential-assets-in-the-background)*