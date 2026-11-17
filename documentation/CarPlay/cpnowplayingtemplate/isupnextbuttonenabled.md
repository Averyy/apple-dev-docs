# isUpNextButtonEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Now Playing interface displays the Up Next button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isUpNextButtonEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isUpNextButtonEnabled) BOOL upNextButtonEnabled;
```

## Discussion

When the value of this property is `true`, the Now Playing interface displays an Up Next button in the upper-right corner of the Now Playing interface. This button provides access to content that’s queued and ready for playback. The default value of this property is `false`.

If you set this property to `true`, add an observer object to the Now Playing template. When someone taps the Up Next button, the template calls your observer’s  `CPNowPlayingTemplateDelegate/nowPlayingTemplateUpNextButtonTapped(_:)` method to notify you of the interaction.

## See Also

### Configuring the interface
- [var nowPlayingMode: CPNowPlayingMode?](./nowplayingmode.md)
  The type that determines the layout of the Now Playing interface.
- [var upNextTitle: String](./upnexttitle.md)
  The text to display in the Up Next button.
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist information is a tappable button.
- [var allowsMiniPlayer: Bool](./allowsminiplayer.md)
  A Boolean value that indicates whether the app supports the mini-player interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/isupnextbuttonenabled)*