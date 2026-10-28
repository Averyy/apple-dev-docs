# mediaType

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of the asset, such as video or audio.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var mediaType: PHAssetMediaType { get }
```

```objc
@property (assign, readonly) PHAssetMediaType mediaType;
```

## Discussion

See [`PHAssetMediaType`](../phassetmediatype.md) for possible values.

## See Also

### Getting Information About the Asset
- [enum PHAssetMediaType](../phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [var mediaSubtypes: PHAssetMediaSubtype](./mediasubtypes.md)
  The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [struct PHAssetMediaSubtype](../phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var creationDate: Date?](./creationdate.md)
  The date and time when the asset was originally created.
- [var location: CLLocation?](./location.md)
  The location information that was saved with the asset.
- [var uniformTypeIdentifier: String?](./uniformtypeidentifier.md)
  The uniform type identifier for the asset’s image or video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/mediatype)*