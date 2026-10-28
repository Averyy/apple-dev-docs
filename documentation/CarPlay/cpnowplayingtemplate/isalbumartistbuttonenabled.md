# isAlbumArtistButtonEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the album and artist string is a button.

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

The Now Playing template displays a string above the playback control buttons that contains the album and artist names. Set this property to [`true`](../../Swift/true.md) to turn the string into a button that you can use to present more information about the current track. To respond to a user tapping the button, create an object that conforms to [`CPNowPlayingTemplateObserver`](../cpnowplayingtemplateobserver.md) and register it with the Now Playing template using the template’s [`add(_:)`](./add%28_%29.md) method.

The default value is [`false`](../../Swift/false.md).

## See Also

### Managing Albums, Artists, and Up Next
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that manages the display of the Up Next button.
- [var upNextTitle: String](./upnexttitle.md)
  The title for the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/isalbumartistbuttonenabled)*