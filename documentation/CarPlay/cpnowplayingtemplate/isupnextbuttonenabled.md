# isUpNextButtonEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that manages the display of the Up Next button.

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

Set this property to [`true`](../../Swift/true.md) to have the Now Playing template display an Up Next button in the upper-right corner of the CarPlay screen.

The default value is [`false`](../../Swift/false.md).

## See Also

### Managing Albums, Artists, and Up Next
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist string is a button.
- [var upNextTitle: String](./upnexttitle.md)
  The title for the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/isupnextbuttonenabled)*