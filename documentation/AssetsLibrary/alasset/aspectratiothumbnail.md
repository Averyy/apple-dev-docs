# aspectRatioThumbnail()

**Framework**: Assets Library  
**Kind**: method

Returns an aspect ratio thumbnail of the asset.

## Declaration

```swift
func aspectRatioThumbnail() -> Unmanaged<CGImage>!
```

#### Return Value

An aspect ratio thumbnail of the asset.

#### Discussion

Returns a CGImage with an aspect ratio thumbnail of the asset. The size of the thumbnail is the appropriate size for the platform, and in the correct orientation.

This method returns `NULL` for assets from a shared photo stream that are not yet available locally. If the asset becomes available in the future, an [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification is posted.

## See Also

- [func defaultRepresentation() -> ALAssetRepresentation!](alasset/defaultrepresentation.md)
  Returns an asset representation object for the default representation.
- [func representation(forUTI: String!) -> ALAssetRepresentation!](alasset/representation(foruti:).md)
  Returns an asset representation object for a given representation UTI.
- [func thumbnail() -> Unmanaged<CGImage>!](alasset/thumbnail.md)
  Returns a thumbnail representation of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/aspectratiothumbnail())*