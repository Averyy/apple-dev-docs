# nowPlayingButtons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional app-specific playback controls to display in the lower region of the Now Playing interface.

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

This property contains the buttons for any additional features your app supports during playback. The template places the buttons in the lower region of the interface starting at the leading edge, and displays them in the same order as they appear in the array.

The default value of this property is an empty array. To specify buttons for your interface, call the [`updateNowPlayingButtons(_:)`](./updatenowplayingbuttons%28_%29.md) method. For example, you might include buttons to shuffle the queued songs, repeat songs, or change the playback rate.

## See Also

### Adding app-specific controls
- [func updateNowPlayingButtons([CPNowPlayingButton])](./updatenowplayingbuttons%28_%29.md)
  Updates the app-specific playback controls that appear in the lower region of the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/nowplayingbuttons)*