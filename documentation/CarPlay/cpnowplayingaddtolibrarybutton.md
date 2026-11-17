# CPNowPlayingAddToLibraryButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button for adding the current item to a collection, such as the person’s library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingAddToLibraryButton
```

```objc
@interface CPNowPlayingAddToLibraryButton : CPNowPlayingButton
```

## Overview

Include the `CPNowPlayingAddToLibraryButton ` in your Now Playing template if your app supports adding items to playlists or other collections. The system provides the appearance of the button. Respond to button interactions by adding the item to the appropriate collection in your app.

Create the button and add it as one of the [`nowPlayingButtons`](./cpnowplayingtemplate/nowplayingbuttons.md) in your Now Playing template. At creation time, provide a handler you want the system to call when someone interacts with the button, and use your handler to update your app’s data structures.

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

## See Also

### Now Playing buttons
- [class CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
  A button for toggling shuffle mode on and off.
- [class CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
  A button for changing the playback rate of the media.
- [class CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
  A button for displaying additional playback options.
- [class CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
  A custom Now Playing button that displays an image.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class for buttons in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingaddtolibrarybutton)*