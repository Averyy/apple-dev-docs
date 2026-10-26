# init(for:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(for asset: PHAsset)
```

```objc
+ (instancetype) changeRequestForAsset:(PHAsset *) asset;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Return Value

An asset change request.

#### Discussion

Before editing an asset, use its [`canPerform(_:)`](../phasset/canperform%28_%29.md) method to see if the asset allows editing.

After you create a change request within a photo library change block, propose changes to the original asset’s properties by setting the corresponding properties of the change request. After Photos runs your change block, the asset’s properties reflect your changes. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

To edit an asset’s image or video content, first begin a content editing session with the asset’s [`requestContentEditingInput(with:completionHandler:)`](../phasset/requestcontenteditinginput%28with,completionhandler%29.md) method. You commit a content edit by setting the [`contentEditingOutput`](./contenteditingoutput.md) property of a change request within a change block. For more information about asset content editing, see [`PHAsset`](../phasset.md).

## Parameters

- `asset`: The asset to be modified.

## See Also

### Modifying Assets
- [var creationDate: Date?](./creationdate.md)
  The date and time at which the asset claims to have been originally created.
- [var location: CLLocation?](./location.md)
  The location information saved with the asset.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that indicates whether the asset is hidden in collections.
- [var caption: String?](./caption.md)
  An asset description to change to. Set to nil or an empty string to clear the caption.
- [func addKeyword(String)](./addkeyword%28_%29.md)
  Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored
- [func removeKeyword(String)](./removekeyword%28_%29.md)
- [var rating: PHAsset.Rating](./rating.md)
  The rating for this asset
- [func setLivePhotoVideoPlaybackEnabled(Bool)](./setlivephotovideoplaybackenabled%28_%29.md)
  Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/init(for:))*