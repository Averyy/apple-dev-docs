# CPNowPlayingPlaybackRateButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button for changing the playback rate of the media.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingPlaybackRateButton
```

```objc
@interface CPNowPlayingPlaybackRateButton : CPNowPlayingButton
```

## Overview

Include the `CPNowPlayingRepeatButton ` in your Now Playing template if your app supports different playback rates for content. The system provides the appearance of the button and automatically updates the appearance to reflect the playback rate of the current media file. When someone interacts with the button, respond by changing the playback rate programmatically from your app.

Create the button and add it as one of the [`nowPlayingButtons`](./cpnowplayingtemplate/nowplayingbuttons.md) in your Now Playing template. At creation time, provide a handler you want the system to call when someone interacts with the button, and use your handler to change the current playback speed.

> **Note**: CarPlay uses the shared [`MPRemoteCommandCenter`](../MediaPlayer/mpremotecommandcenter.md) object to observe changes to the playback rate and update the button’s appearance. If your app supports the command center object, provide the same behavior in your button’s handler as you provide for the [`MPChangePlaybackRateCommand`](../MediaPlayer/mpchangeplaybackratecommand.md) type.

## Relationships

### Inherits From
- [CPNowPlayingButton](./cpnowplayingbutton.md)
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

### Now Playing buttons
- [class CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
  A button for toggling shuffle mode on and off.
- [class CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
  A button for adding the current item to a collection, such as the person’s library.
- [class CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
  A button for displaying additional playback options.
- [class CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
  A custom Now Playing button that displays an image.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class for buttons in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingplaybackratebutton)*