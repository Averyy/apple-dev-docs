# representation(forUTI:)

**Framework**: Assets Library  
**Kind**: method

Returns an asset representation object for a given representation UTI.

## Declaration

```swift
func representation(forUTI representationUTI: String!) -> ALAssetRepresentation!
```

#### Return Value

An an asset representation object for the representation specified by `representationUTI`, or `nil` if the asset does not support the representation.

#### Discussion

This method returns `nil` for assets from a shared photo stream that are not yet available locally. If the asset becomes available in the future, an [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification is posted.

## Parameters

- `representationUTI`: A UTI describing a representation for the asset.

## See Also

- [func defaultRepresentation() -> ALAssetRepresentation!](alasset/defaultrepresentation.md)
  Returns an asset representation object for the default representation.
- [func thumbnail() -> Unmanaged<CGImage>!](alasset/thumbnail.md)
  Returns a thumbnail representation of the asset.
- [func aspectRatioThumbnail() -> Unmanaged<CGImage>!](alasset/aspectratiothumbnail.md)
  Returns an aspect ratio thumbnail of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/representation(foruti:))*