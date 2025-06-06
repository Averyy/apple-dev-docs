# ALAssetsGroupFaces

**Framework**: Assets Library  
**Kind**: var

All the faces albums synced from iTunes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var ALAssetsGroupFaces: UInt32 { get }
```

## See Also

- [var ALAssetsGroupLibrary: UInt32](alassetsgrouplibrary.md)
  The Library group that includes all assets that are synced from iTunes.
- [var ALAssetsGroupAlbum: UInt32](alassetsgroupalbum.md)
  All the albums created on the device or synced from iTunes, not including Photo Stream or Shared Streams
- [var ALAssetsGroupEvent: UInt32](alassetsgroupevent.md)
  All events, including those created during Camera Connection Kit import.
- [var ALAssetsGroupSavedPhotos: UInt32](alassetsgroupsavedphotos.md)
  All the photos in the Camera Roll.
- [var ALAssetsGroupPhotoStream: UInt32](alassetsgroupphotostream.md)
  The PhotoStream album.
- [var ALAssetsGroupAll: UInt32](alassetsgroupall.md)
  The same as ORing together all the group types except for [`ALAssetsGroupLibrary`](alassetsgrouplibrary.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroupfaces)*