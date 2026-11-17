# CPNowPlayingMoreButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button for displaying additional playback options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingMoreButton
```

```objc
@interface CPNowPlayingMoreButton : CPNowPlayingButton
```

## Overview

Include a `CPNowPlayingMoreButton` object in your Now Playing template if your app can display additional options. The system provides the appearance of the button, and you provide the button’s response in a custom handler. Use your handler to display additional content relevant to your app. For example, if your app is playing a podcast, you might display information about the podcast using an alert template.

Create the button and add it as one of the [`nowPlayingButtons`](./cpnowplayingtemplate/nowplayingbuttons.md) in your Now Playing template. At creation time, provide the handler you want the system to call when someone interacts with the button.

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
- [class CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
  A button for changing the playback rate of the media.
- [class CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
  A button for adding the current item to a collection, such as the person’s library.
- [class CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
  A custom Now Playing button that displays an image.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class for buttons in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmorebutton)*