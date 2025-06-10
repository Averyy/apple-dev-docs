# ALAssetsGroupPhotoStream

**Framework**: Assets Library  
**Kind**: var

The PhotoStream album.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var ALAssetsGroupPhotoStream: UInt32 { get }
```

#### Discussion

In iOS 6.0 and later, this also includes Shared Streams.

## See Also

- [var ALAssetsGroupLibrary: UInt32](alassetsgrouplibrary.md)
  The Library group that includes all assets that are synced from iTunes.
- [var ALAssetsGroupAlbum: UInt32](alassetsgroupalbum.md)
  All the albums created on the device or synced from iTunes, not including Photo Stream or Shared Streams
- [var ALAssetsGroupEvent: UInt32](alassetsgroupevent.md)
  All events, including those created during Camera Connection Kit import.
- [var ALAssetsGroupFaces: UInt32](alassetsgroupfaces.md)
  All the faces albums synced from iTunes.
- [var ALAssetsGroupSavedPhotos: UInt32](alassetsgroupsavedphotos.md)
  All the photos in the Camera Roll.
- [var ALAssetsGroupAll: UInt32](alassetsgroupall.md)
  The same as ORing together all the group types except for [`ALAssetsGroupLibrary`](alassetsgrouplibrary.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroupphotostream)*