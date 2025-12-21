# ALAssetRepresentation

**Framework**: Assets Library  
**Kind**: class

An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.

## Declaration

```swift
class ALAssetRepresentation
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset) and [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager) classes provide functionality for fetching an asset’s image or video data.

A given asset in the library may have more than one representation. For example, if a camera provides RAW and JPEG versions of an image, the resulting asset will have two representations—one for the RAW file and one for the JPEG file.

## Topics

### Getting Image Representations
- [func cgImage(options: [AnyHashable : Any]!) -> Unmanaged<CGImage>!](alassetrepresentation/cgimage(options:).md)
  Returns a full resolution CGImage of the representation.
- [func fullResolutionImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullresolutionimage.md)
  Returns a CGImage representation of the asset.
- [func fullScreenImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullscreenimage.md)
  Returns a CGImage of the representation that is appropriate for displaying full screen.
### Getting Image Attributes
- [func orientation() -> ALAssetOrientation](alassetrepresentation/orientation.md)
  Returns the representation’s orientation.
- [func scale() -> Float](alassetrepresentation/scale.md)
  Returns the representation’s scale.
- [func dimensions() -> CGSize](alassetrepresentation/dimensions.md)
  Returns the representation’s dimensions.
- [func filename() -> String!](alassetrepresentation/filename.md)
  Returns a string representing the filename of the representation on disk.
### Getting Raw Data
- [func size() -> Int64](alassetrepresentation/size.md)
  Returns the size in bytes of the file for the representation.
- [func getBytes(UnsafeMutablePointer<UInt8>!, fromOffset: Int64, length: Int, error: NSErrorPointer) -> Int](alassetrepresentation/getbytes(_:fromoffset:length:error:).md)
  Copies a specified range of bytes into a given buffer.
### Getting Metadata
- [func uti() -> String!](alassetrepresentation/uti.md)
  Returns the representation’s UTI.
- [func metadata() -> [AnyHashable : Any]!](alassetrepresentation/metadata.md)
  Returns a dictionary of dictionaries of metadata for the representation.
### Getting an URL
- [func url() -> URL!](alassetrepresentation/url.md)
  Returns a persistent URL uniquely identifying the representation.

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

- [class ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [class ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [class ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [class ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation)*