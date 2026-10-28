# locationCreated

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location where someone took the photos.

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
var locationCreated: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * locationCreated;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * locationCreated;
```

## Discussion

Use the placemark information to limit the scope of your search to photos in the given area. Define the area as precisely as you can given the available information. For example, if the placemark includes a specific address, limit your search to photos taken at that address.

## See Also

### Getting the Search Attributes
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates during which someone took the pictures.
- [var albumName: String?](./albumname.md)
  The name of the album that contains the photos.
- [var includedAttributes: INPhotoAttributeOptions](./includedattributes.md)
  The attributes that must be present in the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./excludedattributes.md)
  The attributes that must not be present in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/locationcreated)*