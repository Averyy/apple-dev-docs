# includedAttributes

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The attributes that must be present in the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var includedAttributes: INPhotoAttributeOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INPhotoAttributeOptions includedAttributes;
```

*macOS*

```objc
@property (atomic, assign, readonly) INPhotoAttributeOptions includedAttributes;
```

#### Discussion

All of the specified attributes must be present in the photos.

## See Also

### Getting the Search Attributes
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates during which someone took the pictures.
- [var locationCreated: CLPlacemark?](./locationcreated.md)
  The location where someone took the photos.
- [var albumName: String?](./albumname.md)
  The name of the album that contains the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./excludedattributes.md)
  The attributes that must not be present in the photos.
- [struct INPhotoAttributeOptions](../inphotoattributeoptions.md)
  Constants indicating attributes of a photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintent/includedattributes)*