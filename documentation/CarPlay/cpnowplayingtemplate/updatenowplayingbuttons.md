# updateNowPlayingButtons(_:)

**Framework**: CarPlay  
**Kind**: method

Updates the playback control buttons the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func updateNowPlayingButtons(_ nowPlayingButtons: [CPNowPlayingButton])
```

#### Discussion

You can provide a maximum of five playback control buttons. The template arranges the buttons using the array’s order, from the leading edge of the CarPlay screen to the trailing edge.

## Parameters

- `nowPlayingButtons`: The array of buttons to display.

## See Also

- [var nowPlayingButtons: [CPNowPlayingButton]](cpnowplayingtemplate/nowplayingbuttons.md)
  The Now Playing template’s playback control buttons.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/updatenowplayingbuttons(_:))*