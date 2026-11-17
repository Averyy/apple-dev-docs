# allowsMiniPlayer

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app supports the mini-player interface.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var allowsMiniPlayer: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsMiniPlayer;
```

## Discussion

When the Now Playing template isn’t visible, the system adds a mini-player interface to the navigation bar of your app’s other templates. This interface summarizes the currently playing content and offers a way to start and stop playback, change tracks, and navigate back to the Now Playing interface. If your app has its own compact interface for currently playing content, you can set this property to `false` to disable the system-provided miniature interface. The default value of this property is `true`, which displays the mini-player interface in your other templates.

## See Also

### Configuring the interface
- [var nowPlayingMode: CPNowPlayingMode?](./nowplayingmode.md)
  The type that determines the layout of the Now Playing interface.
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that indicates whether the Now Playing interface displays the Up Next button.
- [var upNextTitle: String](./upnexttitle.md)
  The text to display in the Up Next button.
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist information is a tappable button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/allowsminiplayer)*