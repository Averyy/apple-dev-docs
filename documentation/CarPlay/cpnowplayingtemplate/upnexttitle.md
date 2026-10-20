# upNextTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title for the Up Next button.

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

#### Discussion

If you display the Up Next button in your app by setting [`isUpNextButtonEnabled`](./isupnextbuttonenabled.md) to [`true`](../../Swift/true.md), use this property to set the button’s title. If you don’t specify a title, CarPlay uses the system default title.

## See Also

### Managing Albums, Artists, and Up Next
- [var isAlbumArtistButtonEnabled: Bool](./isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist string is a button.
- [var isUpNextButtonEnabled: Bool](./isupnextbuttonenabled.md)
  A Boolean value that manages the display of the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/upnexttitle)*