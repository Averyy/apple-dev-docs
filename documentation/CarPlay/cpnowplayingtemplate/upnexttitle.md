# upNextTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The text to display in the Up Next button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var upNextTitle: String { get set }
```

```objc
@property (nonatomic, copy) NSString * upNextTitle;
```

## Discussion

Set this property to the text you want to display in the Up Next button of the Now Playing interface. When the [`isUpNextButtonEnabled`](./isupnextbuttonenabled.md) property is `true`, the system displays the button and sets its title to the provided text. If you don’t specify a value for this property, the system supplies a default value for the button title.

## See Also

### Configuring the interface
- [var nowPlayingMode: CPNowPlayingMode?](./nowplayingmode.md)
  The type that determines the layout of the Now Playing interface.
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that indicates whether the Now Playing interface displays the Up Next button.
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist information is a tappable button.
- [var allowsMiniPlayer: Bool](./allowsminiplayer.md)
  A Boolean value that indicates whether the app supports the mini-player interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/upnexttitle)*