# CPNowPlayingTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A shared system template that shows the currently selected audio content and offers controls to manage playback.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingTemplate
```

```objc
@interface CPNowPlayingTemplate : CPTemplate
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

Apps that play audio or video content update the `CPNowPlayingTemplate` to reflect their current and queued content. When visible, the default template layout shows information about the currently playing item and offers controls for someone to start and stop playback, play the next queued item, and manage other playback-related features. If your app manages sports content, you can change the layout to show team and score information for a live or prerecorded sporting event.

Access the shared `CPNowPlayingTemplate` from the [`shared`](./cpnowplayingtemplate/shared.md) property and configure it when your CarPlay app launches. You can push the Now Playing template onto your app’s navigation stack, but the system also displays it in other situations. For example, the Now Playing app shows the interface from the app responsible for the most recently played content. Configuring the template at launch time ensures it’s available when the system needs it. The actual configuration of the template depends on the features you support. If you support the Album Artist or Up Next buttons, call the [`add(_:)`](./cpnowplayingtemplate/add%28_%29.md) method to register an observer to respond to interactions with those buttons.

To provide the Now Playing interface with information about the media you’re playing, play your media using the types of the [Media Player](../MediaPlayer/MediaPlayer.md) and [AVKit](../AVKit/AVKit.md) frameworks. Each framework has its own form of Now Playing support, which CarPlay uses to populate the template. For example, a type like [`MPMusicPlayerController`](../MediaPlayer/mpmusicplayercontroller.md) manages a queue of songs to play, and communicates the current and next song directly to the Now Playing interface. CarPlay also starts and stops playback and performs other media-related tasks using the framework types.

When designing your interface hierarchy, you typically don’t push other templates on top of the Now Playing interface. However, if you support the Up Next button, you can push a list template with the queued items on top of the `CPNowPlayingTemplate` type. Don’t push other types of templates.

> **Note**: Audio, video, communication, and public safety apps can display the Now Playing template. You can’t use this template from other types of apps.

## Topics

### Managing the shared template
- [class var shared: CPNowPlayingTemplate](./cpnowplayingtemplate/shared.md)
  The shared Now Playing template for you to configure and display.
### Configuring the interface
- [var nowPlayingMode: CPNowPlayingMode?](./cpnowplayingtemplate/nowplayingmode.md)
  The type that determines the layout of the Now Playing interface.
- [var isUpNextButtonEnabled: Bool](./cpnowplayingtemplate/isupnextbuttonenabled.md)
  A Boolean value that indicates whether the Now Playing interface displays the Up Next button.
- [var upNextTitle: String](./cpnowplayingtemplate/upnexttitle.md)
  The text to display in the Up Next button.
- [var isAlbumArtistButtonEnabled: Bool](./cpnowplayingtemplate/isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist information is a tappable button.
- [var allowsMiniPlayer: Bool](./cpnowplayingtemplate/allowsminiplayer.md)
  A Boolean value that indicates whether the app supports the mini-player interface.
### Adding app-specific controls
- [var nowPlayingButtons: [CPNowPlayingButton]](./cpnowplayingtemplate/nowplayingbuttons.md)
  Additional app-specific playback controls to display in the lower region of the Now Playing interface.
- [func updateNowPlayingButtons([CPNowPlayingButton])](./cpnowplayingtemplate/updatenowplayingbuttons%28_%29.md)
  Updates the app-specific playback controls that appear in the lower region of the Now Playing interface.
### Adding and removing observers
- [func add(any CPNowPlayingTemplateObserver)](./cpnowplayingtemplate/add%28_%29.md)
  Registers an observer to handle events related to the Now Playing interface.
- [func remove(any CPNowPlayingTemplateObserver)](./cpnowplayingtemplate/remove%28_%29.md)
  Unregisters an observer and stops it from receiving events related to the Now Playing interface.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface templates
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate)*