# dateCreated

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of dates during which someone took the pictures.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var dateCreated: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dateCreated;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dateCreated;
```

#### Discussion

Use this property to limit the scope of the search to photos taken within the specified dates.

## See Also

### Getting the Search Attributes
- [var locationCreated: CLPlacemark?](./locationcreated.md)
  The location where someone took the photos.
- [var albumName: String?](./albumname.md)
  The name of the album that contains the photos.
- [var includedAttributes: INPhotoAttributeOptions](./includedattributes.md)
  The attributes that must be present in the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./excludedattributes.md)
  The attributes that must not be present in the photos.
- [struct INPhotoAttributeOptions](../inphotoattributeoptions.md)
  Constants indicating attributes of a photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintent/datecreated)*