# init(dateCreated:locationCreated:albumName:searchTerms:includedAttributes:excludedAttributes:peopleInPhoto:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent object with the specified search parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(dateCreated: INDateComponentsRange?, locationCreated: CLPlacemark?, albumName: String?, searchTerms: [String]?, includedAttributes: INPhotoAttributeOptions = [], excludedAttributes: INPhotoAttributeOptions = [], peopleInPhoto: [INPerson]?)
```

```objc
- (instancetype) initWithDateCreated:(INDateComponentsRange *) dateCreated locationCreated:(CLPlacemark *) locationCreated albumName:(NSString *) albumName searchTerms:(NSArray<NSString *> *) searchTerms includedAttributes:(INPhotoAttributeOptions) includedAttributes excludedAttributes:(INPhotoAttributeOptions) excludedAttributes peopleInPhoto:(NSArray<INPerson *> *) peopleInPhoto;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks to start a slideshow. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `dateCreated`: The range of date stamps of the photos.
- `locationCreated`: The geographic location of the photos.
- `albumName`: The name of the album that contains the photos.
- `searchTerms`: An array of terms to look for in the photo. These terms can refer to tags, keywords, descriptions, or names of people associated with the photo.
- `includedAttributes`: The attributes that are present in the photos. This parameter may contain multiple attributes.
- `excludedAttributes`: The attributes that aren’t present in the photos. This parameter may contain multiple attributes.
- `peopleInPhoto`: One or more users present in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/init(datecreated:locationcreated:albumname:searchterms:includedattributes:excludedattributes:peopleinphoto:))*