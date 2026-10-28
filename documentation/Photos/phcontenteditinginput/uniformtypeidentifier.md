# uniformTypeIdentifier

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The uniform type identifier for the asset’s image or video data.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.11+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use contentType instead

## Declaration

```swift
var uniformTypeIdentifier: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * uniformTypeIdentifier;
```

## Discussion

For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Getting Information About the Asset
- [var mediaType: PHAssetMediaType](./mediatype.md)
  The type of the asset, such as video or audio.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/uniformtypeidentifier)*