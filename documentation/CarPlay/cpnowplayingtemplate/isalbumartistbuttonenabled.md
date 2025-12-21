# isAlbumArtistButtonEnabled

**Framework**: CarPlay  
**Kind**: property

A Boolean value that indicates whether the album and artist string is a button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var isAlbumArtistButtonEnabled: Bool { get set }
```

#### Discussion

The Now Playing template displays a string above the playback control buttons that contains the album and artist names. Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to turn the string into a button that you can use to present more information about the current track. To respond to a user tapping the button, create an object that conforms to [`CPNowPlayingTemplateObserver`](cpnowplayingtemplateobserver.md) and register it with the Now Playing template using the template’s [`add(_:)`](cpnowplayingtemplate/add(_:).md) method.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isUpNextButtonEnabled: Bool](cpnowplayingtemplate/isupnextbuttonenabled.md)
  A Boolean value that manages the display of the Up Next button.
- [var upNextTitle: String](cpnowplayingtemplate/upnexttitle.md)
  The title for the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/isalbumartistbuttonenabled)*