# nowPlayingButtons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The Now Playing template’s playback control buttons.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var nowPlayingButtons: [CPNowPlayingButton] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<__kindof CPNowPlayingButton *> * nowPlayingButtons;
```

## Discussion

You use the [`updateNowPlayingButtons(_:)`](./updatenowplayingbuttons%28_%29.md) method to provide a maximum of five playback control buttons. The template arranges the buttons using the array’s order, from the leading edge of the CarPlay screen to the trailing edge.

## See Also

### Managing the Template’s Buttons
- [func updateNowPlayingButtons([CPNowPlayingButton])](./updatenowplayingbuttons%28_%29.md)
  Updates the playback control buttons the template displays.
- [class CPNowPlayingButton](../cpnowplayingbutton.md)
  The abstract base class that Now Playing template buttons use.
- [class CPNowPlayingImageButton](../cpnowplayingimagebutton.md)
  A button that displays an image.
- [class CPNowPlayingAddToLibraryButton](../cpnowplayingaddtolibrarybutton.md)
  A button for adding the current playing item to a collection.
- [class CPNowPlayingMoreButton](../cpnowplayingmorebutton.md)
  A button for presenting more options to the user.
- [class CPNowPlayingPlaybackRateButton](../cpnowplayingplaybackratebutton.md)
  A button for cycling through the available playback rates.
- [class CPNowPlayingRepeatButton](../cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingShuffleButton](../cpnowplayingshufflebutton.md)
  A button for cycling through the available shuffle modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/nowplayingbuttons)*