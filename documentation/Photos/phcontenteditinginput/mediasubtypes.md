# mediaSubtypes

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var mediaSubtypes: PHAssetMediaSubtype { get }
```

```objc
@property (assign, readonly) PHAssetMediaSubtype mediaSubtypes;
```

#### Discussion

See [`PHAssetMediaSubtype`](../phassetmediasubtype.md) for possible values.

Because an asset can have more than one subtype, use these values as bit masks to identify an asset. For example, the code below tests an asset for the panorama photo subtype.

**Swift**:

```swift
if asset.mediaType == .image && ((asset.mediaSubtypes.rawValue & PHAssetMediaSubtype.photoHDR.rawValue) != 0) {
    // Display an HDR badge in the user interface.
}
```

**Objective-C**:

```objc
if (contentEditingInput.mediaType == PHAssetMediaTypeImage
    && (contentEditingInput.mediaSubtypes & PHAssetMediaSubtypePhotoHDR)) {
    // Display an HDR badge in the user interface.
}
```

## See Also

### Getting Information About the Asset
- [var mediaType: PHAssetMediaType](./mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](../phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [struct PHAssetMediaSubtype](../phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var creationDate: Date?](./creationdate.md)
  The date and time when the asset was originally created.
- [var location: CLLocation?](./location.md)
  The location information that was saved with the asset.
- [var uniformTypeIdentifier: String?](./uniformtypeidentifier.md)
  The uniform type identifier for the asset’s image or video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/mediasubtypes)*