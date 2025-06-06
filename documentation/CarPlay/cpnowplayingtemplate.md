# CPNowPlayingTemplate

**Framework**: CarPlay  
**Kind**: class

A shared system template that displays Now Playing information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPNowPlayingTemplate
```

#### Overview

The Now Playing template displays information from [`MPNowPlayingInfoCenter`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingInfoCenter) and [`MPNowPlayingSession`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingSession). Instead of instantiating your own Now Playing template, CarPlay provides a shared instance that you configure. The template displays a series of playback control buttons, as well as information about the current album and artist, and what’s coming up next.

When enabling your Now Playing template’s Album-Artist and Up Next buttons, you must create an object that implements the [`CPNowPlayingTemplateObserver`](cpnowplayingtemplateobserver.md) protocol and register it as an observer by calling the template’s [`add(_:)`](cpnowplayingtemplate/add(_:).md) method.

To display the Now Playing template, call your interface controller’s [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) method to push it onto your navigation hierarchy. You can’t display the Now Playing template modally.

When CarPlay presents Now Playing information for your app, it uses the shared instance of this template.

> **Note**:  `CPNowPlayingTemplate` is only available in apps with the audio entitlement.

 `CPNowPlayingTemplate` is only available in apps with the audio entitlement.

## Topics

### Managing the Shared Template
- [class var shared: CPNowPlayingTemplate](cpnowplayingtemplate/shared.md)
  The Now Playing template the system provides.
### Managing the Template’s Buttons
- [var nowPlayingButtons: [CPNowPlayingButton]](cpnowplayingtemplate/nowplayingbuttons.md)
  The Now Playing template’s playback control buttons.
- [func updateNowPlayingButtons([CPNowPlayingButton])](cpnowplayingtemplate/updatenowplayingbuttons(_:).md)
  Updates the playback control buttons the template displays.
- [class CPNowPlayingButton](cpnowplayingbutton.md)
  The abstract base class that Now Playing template buttons use.
- [class CPNowPlayingImageButton](cpnowplayingimagebutton.md)
  A button that displays an image.
- [class CPNowPlayingAddToLibraryButton](cpnowplayingaddtolibrarybutton.md)
  A button for adding the current playing item to a collection.
- [class CPNowPlayingMoreButton](cpnowplayingmorebutton.md)
  A button for presenting more options to the user.
- [class CPNowPlayingPlaybackRateButton](cpnowplayingplaybackratebutton.md)
  A button for cycling through the available playback rates.
- [class CPNowPlayingRepeatButton](cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingShuffleButton](cpnowplayingshufflebutton.md)
  A button for cycling through the available shuffle modes.
### Managing Albums, Artists, and Up Next
- [var isAlbumArtistButtonEnabled: Bool](cpnowplayingtemplate/isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist string is a button.
- [var isUpNextButtonEnabled: Bool](cpnowplayingtemplate/isupnextbuttonenabled.md)
  A Boolean value that manages the display of the Up Next button.
- [var upNextTitle: String](cpnowplayingtemplate/upnexttitle.md)
  The title for the Up Next button.
### Observing Now Playing Events
- [func add(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/add(_:).md)
  Registers an observer that receives Now Playing template events.
- [func remove(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/remove(_:).md)
  Removes an observer from receiving Now Playing template events.
- [protocol CPNowPlayingTemplateObserver](cpnowplayingtemplateobserver.md)
  The methods for responding to the user interacting with the Now Playing template.
### Instance Properties
- [var nowPlayingMode: CPNowPlayingMode?](cpnowplayingtemplate/nowplayingmode.md)
  The currently-active now playing mode. See @c CPNowPlayingMode.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Integrating CarPlay with Your Music App](integrating-carplay-with-your-music-app.md)
  Configure your music app to work with CarPlay by displaying a custom UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate)*