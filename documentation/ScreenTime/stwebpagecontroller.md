# STWebpageController

**Framework**: Screen Time  
**Kind**: class  
**Role**: Class

The controller you use to report web usage and block restricted webpages.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class STWebpageController
```

*iOS, iPadOS, Mac Catalyst*

```objc
@interface STWebpageController : UIViewController
```

*macOS*

```objc
@interface STWebpageController : NSViewController
```

## Overview

This class provides a convenient way for you to communicate changes in each webpage, such as when the user starts or stops playing media. When a parent or guardian of the user blocks the webpage’s current URL, the webpage controller:

- Automatically occludes the web page’s content
- Updates a KVO-compliant [`urlIsBlocked`](./stwebpagecontroller/urlisblocked.md) property

For example, you can observe `urlIsBlocked` and take action when it changes to [`YES`](../ObjectiveC/yes.md), such as pausing media.

> ❗ **Important**: Create a webpage controller for each webpage or tab and add it on top of the webpage’s content.

## Topics

### Instance properties
- [var suppressUsageRecording: Bool](./stwebpagecontroller/suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var url: URL?](./stwebpagecontroller/url.md)
  The URL for the webpage.
- [var urlIsBlocked: Bool](./stwebpagecontroller/urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPictureInPicture: Bool](./stwebpagecontroller/urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.
- [var urlIsPlayingVideo: Bool](./stwebpagecontroller/urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.
### Instance methods
- [func setBundleIdentifier(String) throws](./stwebpagecontroller/setbundleidentifier%28_%29.md)
  Changes the bundle identifier used to report web usage.
### Instance Properties
- [var profileIdentifier: STWebHistory.ProfileIdentifier?](./stwebpagecontroller/profileidentifier.md)
  An optional identifier for the current browsing profile.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller)*