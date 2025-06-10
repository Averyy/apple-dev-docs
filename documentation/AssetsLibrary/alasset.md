# ALAsset

**Framework**: Assets Library  
**Kind**: class

An `ALAsset` object represents a photo or a video managed by the Photo application.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ALAsset
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset) class provides functionality for fetching and working with photo and video assets.

Assets can have multiple representations, for example a photo which was captured in RAW and JPG. Different representations of the same asset may have different dimensions.

## Topics

### Asset Properties
- [func value(forProperty: String!) -> Any!](alasset/value(forproperty:).md)
  Returns the value for a given property.
- [var isEditable: Bool](alasset/iseditable.md)
  Indicates whether the asset is editable.
- [var original: ALAsset!](alasset/original.md)
  The original version of the asset.
### Accessing Representations
- [func defaultRepresentation() -> ALAssetRepresentation!](alasset/defaultrepresentation.md)
  Returns an asset representation object for the default representation.
- [func representation(forUTI: String!) -> ALAssetRepresentation!](alasset/representation(foruti:).md)
  Returns an asset representation object for a given representation UTI.
- [func thumbnail() -> Unmanaged<CGImage>!](alasset/thumbnail.md)
  Returns a thumbnail representation of the asset.
- [func aspectRatioThumbnail() -> Unmanaged<CGImage>!](alasset/aspectratiothumbnail.md)
  Returns an aspect ratio thumbnail of the asset.
### Setting New Image and Video Data
- [func setImageData(Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/setimagedata(_:metadata:completionblock:).md)
  Replaces the image data in the receiver with given image data
- [func setVideoAtPath(URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/setvideoatpath(_:completionblock:).md)
  Replaces the video data in receiver with the video at a given URL.
### Saving to the Saved Photos Album
- [func writeModifiedImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/writemodifiedimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Saves image data to the Saved Photos album.
- [func writeModifiedVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/writemodifiedvideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves the video at a specified path to the Saved Photos album.
### Constants
- [Property Keys](property-keys.md)
  Constants for the keys for the properties you can get from an asset.
- [Invalid Property Value](invalid-property-value.md)
  A constant to indicate that a property accessed by [`value(forProperty:)`](alasset/value(forproperty:).md) is invalid.
- [Asset Types](asset-types.md)
  Constants that specify the type of an asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [class ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [class ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [class ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset)*