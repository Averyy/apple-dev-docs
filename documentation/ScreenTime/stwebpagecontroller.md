# STWebpageController

**Framework**: Screen Time  
**Kind**: class

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

#### Overview

This class provides a convenient way for you to communicate changes in each webpage, such as when the user starts or stops playing media. When a parent or guardian of the user blocks the webpage’s current URL, the webpage controller:

- Automatically occludes the web page’s content
- Updates a KVO-compliant [`urlIsBlocked`](stwebpagecontroller/urlisblocked.md) property

For example, you can observe `urlIsBlocked` and take action when it changes to [`YES`](https://developer.apple.com/documentation/objectivec/yes), such as pausing media.

> ❗ **Important**: Create a webpage controller for each webpage or tab and add it on top of the webpage’s content.

## Topics

### Instance properties
- [var suppressUsageRecording: Bool](stwebpagecontroller/suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var url: URL?](stwebpagecontroller/url.md)
  The URL for the webpage.
- [var urlIsBlocked: Bool](stwebpagecontroller/urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPictureInPicture: Bool](stwebpagecontroller/urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.
- [var urlIsPlayingVideo: Bool](stwebpagecontroller/urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.
### Instance methods
- [func setBundleIdentifier(String) throws](stwebpagecontroller/setbundleidentifier(_:).md)
  Changes the bundle identifier used to report web usage.
### Instance Properties
- [var profileIdentifier: STWebHistory.ProfileIdentifier?](stwebpagecontroller/profileidentifier.md)
  An optional identifier for the current browsing profile.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller)*