# CPNowPlayingButton

**Framework**: CarPlay  
**Kind**: class

The abstract base class that Now Playing template buttons use.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingButton
```

#### Overview

`CPNowPlayingButton` is an abstract base class for defining buttons that the Now Playing template displays. It provides the common functionality that’s present in all buttons available to the template.

You don’t use this class directly, or create your own subclasses. Instead, you must use one of the concrete subclasses that the framework provides, such as [`CPNowPlayingImageButton`](cpnowplayingimagebutton.md) or [`CPNowPlayingShuffleButton`](cpnowplayingshufflebutton.md).

## Topics

### Creating a Button
- [init(handler: ((CPNowPlayingButton) -> Void)?)](cpnowplayingbutton/init(handler:).md)
  Creates a Now Playing button that invokes a handler.
### Managing the Button State
- [var isEnabled: Bool](cpnowplayingbutton/isenabled.md)
  A Boolean value that indicates whether the button is in an enabled state.
- [var isSelected: Bool](cpnowplayingbutton/isselected.md)
  A Boolean value that indicates whether the button is in a selected state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPNowPlayingAddToLibraryButton](cpnowplayingaddtolibrarybutton.md)
- [CPNowPlayingImageButton](cpnowplayingimagebutton.md)
- [CPNowPlayingMoreButton](cpnowplayingmorebutton.md)
- [CPNowPlayingPlaybackRateButton](cpnowplayingplaybackratebutton.md)
- [CPNowPlayingRepeatButton](cpnowplayingrepeatbutton.md)
- [CPNowPlayingShuffleButton](cpnowplayingshufflebutton.md)
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

## See Also

- [var nowPlayingButtons: [CPNowPlayingButton]](cpnowplayingtemplate/nowplayingbuttons.md)
  The Now Playing template’s playback control buttons.
- [func updateNowPlayingButtons([CPNowPlayingButton])](cpnowplayingtemplate/updatenowplayingbuttons(_:).md)
  Updates the playback control buttons the template displays.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton)*