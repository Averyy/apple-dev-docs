# albumName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the album that contains the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var albumName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * albumName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * albumName;
```

## Discussion

When this property contains an [`NSString`](../../Foundation/nsstring.md) object, your search should return only photos from the album specified by that string. Apps may register a user’s custom photo album names using the [`INVocabulary`](../invocabulary.md) class. Registering custom names helps the system identify those albums when the user speaks them.

## See Also

### Getting the Search Attributes
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates during which someone took the pictures.
- [var locationCreated: CLPlacemark?](./locationcreated.md)
  The location where someone took the photos.
- [var includedAttributes: INPhotoAttributeOptions](./includedattributes.md)
  The attributes that must be present in the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./excludedattributes.md)
  The attributes that must not be present in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/albumname)*