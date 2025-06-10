# thumbnail()

**Framework**: Assets Library  
**Kind**: method

Returns a thumbnail representation of the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func thumbnail() -> Unmanaged<CGImage>!
```

#### Return Value

A thumbnail representation of the asset.

#### Discussion

The size of the thumbnail is the appropriate for the platform. The image is returned in the correct orientation (that is, “pointing up”—you shouldn’t have to rotate the image).

This method returns `NULL` for assets from a shared photo stream that are not yet available locally. If the asset becomes available in the future, an [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification is posted.

## See Also

- [func defaultRepresentation() -> ALAssetRepresentation!](alasset/defaultrepresentation.md)
  Returns an asset representation object for the default representation.
- [func representation(forUTI: String!) -> ALAssetRepresentation!](alasset/representation(foruti:).md)
  Returns an asset representation object for a given representation UTI.
- [func aspectRatioThumbnail() -> Unmanaged<CGImage>!](alasset/aspectratiothumbnail.md)
  Returns an aspect ratio thumbnail of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/thumbnail())*