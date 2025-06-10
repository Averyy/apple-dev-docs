# CPNowPlayingAddToLibraryButton

**Framework**: CarPlay  
**Kind**: class

A button for adding the current playing item to a collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingAddToLibraryButton
```

#### Overview

`CPNowPlayingAddToLibraryButton` is a concrete subclass of [`CPNowPlayingButton`](cpnowplayingbutton.md). Use this button to allow a user to add the current playing item to a collection, such as their library. You implement this functionality in the button’s handler, or use the handler to invoke existing code that performs this function.

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

## See Also

- [var nowPlayingButtons: [CPNowPlayingButton]](cpnowplayingtemplate/nowplayingbuttons.md)
  The Now Playing template’s playback control buttons.
- [func updateNowPlayingButtons([CPNowPlayingButton])](cpnowplayingtemplate/updatenowplayingbuttons(_:).md)
  Updates the playback control buttons the template displays.
- [class CPNowPlayingButton](cpnowplayingbutton.md)
  The abstract base class that Now Playing template buttons use.
- [class CPNowPlayingImageButton](cpnowplayingimagebutton.md)
  A button that displays an image.
- [class CPNowPlayingMoreButton](cpnowplayingmorebutton.md)
  A button for presenting more options to the user.
- [class CPNowPlayingPlaybackRateButton](cpnowplayingplaybackratebutton.md)
  A button for cycling through the available playback rates.
- [class CPNowPlayingRepeatButton](cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingShuffleButton](cpnowplayingshufflebutton.md)
  A button for cycling through the available shuffle modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingaddtolibrarybutton)*