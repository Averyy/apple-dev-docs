# upNextTitle

**Framework**: CarPlay  
**Kind**: property

The title for the Up Next button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var upNextTitle: String { get set }
```

#### Discussion

If you display the Up Next button in your app by setting [`isUpNextButtonEnabled`](cpnowplayingtemplate/isupnextbuttonenabled.md) to [`true`](https://developer.apple.com/documentation/swift/true), use this property to set the button’s title. If you don’t specify a title, CarPlay uses the system default title.

## See Also

- [var isAlbumArtistButtonEnabled: Bool](cpnowplayingtemplate/isalbumartistbuttonenabled.md)
  A Boolean value that indicates whether the album and artist string is a button.
- [var isUpNextButtonEnabled: Bool](cpnowplayingtemplate/isupnextbuttonenabled.md)
  A Boolean value that manages the display of the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/upnexttitle)*