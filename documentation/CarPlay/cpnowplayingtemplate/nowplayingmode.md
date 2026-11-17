# nowPlayingMode

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The type that determines the layout of the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var nowPlayingMode: CPNowPlayingMode? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPNowPlayingMode * nowPlayingMode;
```

## Discussion

The default value of this property is the [`default`](../cpnowplayingmode/default.md) type, which configures the Now Playing interface to display audio-related content. To change the interface layout, assign a different type to this property. For example, to display sports information, assign a [`CPNowPlayingModeSports`](../cpnowplayingmodesports.md) type with the information you want to display.

## See Also

### Configuring the interface
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that indicates whether the Now Playing interface displays the Up Next button.
- [var upNextTitle: String](./upnexttitle.md)
  The text to display in the Up Next button.
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist information is a tappable button.
- [var allowsMiniPlayer: Bool](./allowsminiplayer.md)
  A Boolean value that indicates whether the app supports the mini-player interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/nowplayingmode)*