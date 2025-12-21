# defaultRepresentation()

**Framework**: Assets Library  
**Kind**: method

Returns an asset representation object for the default representation.

## Declaration

```swift
func defaultRepresentation() -> ALAssetRepresentation!
```

#### Return Value

An asset representation object for the default representation.

#### Discussion

This method returns `nil` for assets from a shared photo stream that are not yet available locally. If the asset becomes available in the future, an [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification is posted.

## See Also

- [func representation(forUTI: String!) -> ALAssetRepresentation!](alasset/representation(foruti:).md)
  Returns an asset representation object for a given representation UTI.
- [func thumbnail() -> Unmanaged<CGImage>!](alasset/thumbnail.md)
  Returns a thumbnail representation of the asset.
- [func aspectRatioThumbnail() -> Unmanaged<CGImage>!](alasset/aspectratiothumbnail.md)
  Returns an aspect ratio thumbnail of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/defaultrepresentation())*