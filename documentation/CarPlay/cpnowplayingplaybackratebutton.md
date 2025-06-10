# CPNowPlayingPlaybackRateButton

**Framework**: CarPlay  
**Kind**: class

A button for cycling through the available playback rates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingPlaybackRateButton
```

#### Overview

`CPNowPlayingPlaybackRateButton` is a concrete subclass of [`CPNowPlayingButton`](cpnowplayingbutton.md). Use the button’s handler to invoke your existing functionality for cycling through playback rates, using the same [`MPChangePlaybackRateCommand`](https://developer.apple.com/documentation/MediaPlayer/MPChangePlaybackRateCommand) that you provide to [`MPRemoteCommandCenter`](https://developer.apple.com/documentation/MediaPlayer/MPRemoteCommandCenter).

CarPlay uses `MPRemoteCommandCenter` to observe changes to the playback rate and updates the button’s appearance accordingly.

## Relationships

### Inherits From
- [CPNowPlayingButton](cpnowplayingbutton.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [class CPNowPlayingRepeatButton](cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingShuffleButton](cpnowplayingshufflebutton.md)
  A button for cycling through the available shuffle modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingplaybackratebutton)*