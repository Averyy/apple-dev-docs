# isAlbumArtistButtonEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the album and artist information is a tappable button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isAlbumArtistButtonEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isAlbumArtistButtonEnabled) BOOL albumArtistButtonEnabled;
```

## Discussion

The Now Playing interface displays album and artist information above the playback controls. When the value of this property is `true`, the interface displays this information using a button that makes the content interactive. When the value of this property is `false`, the system displays the album and artist information as static text. The default value of this property is `false`.

If you set this property to `true`, add an observer object to the Now Playing template. When someone taps the Up Next button, the template calls your observer’s  `CPNowPlayingTemplateDelegate/nowPlayingTemplateAlbumArtistButtonTapped(_:)` method to notify you of the interaction.

## See Also

### Configuring the interface
- [var nowPlayingMode: CPNowPlayingMode?](./nowplayingmode.md)
  The type that determines the layout of the Now Playing interface.
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that indicates whether the Now Playing interface displays the Up Next button.
- [var upNextTitle: String](./upnexttitle.md)
  The text to display in the Up Next button.
- [var allowsMiniPlayer: Bool](./allowsminiplayer.md)
  A Boolean value that indicates whether the app supports the mini-player interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/isalbumartistbuttonenabled)*