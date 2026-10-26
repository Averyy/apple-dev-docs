# INStartPhotoPlaybackIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to search for photos and initiate a slideshow with the results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INStartPhotoPlaybackIntent
```

```objc
@interface INStartPhotoPlaybackIntent : INIntent
```

#### Overview

The system creates an [`INStartPhotoPlaybackIntent`](./instartphotoplaybackintent.md) object when the user asks to start a slideshow of a set of photos. This intent object contains the parameters to use when searching for the photos, including the possible name of a photo album, the people in the photos, or the location of the photos. Use this intent object to perform the search and initiate the slideshow in your app. When performing the search, use only the parameters provided and ignore any that have no values.

To handle this intent, the handler object in your Intents extension must adopt the [`INStartPhotoPlaybackIntentHandling`](./instartphotoplaybackintenthandling.md) protocol. Your handler should confirm the request and create an [`INStartPhotoPlaybackIntentResponse`](./instartphotoplaybackintentresponse.md) object with the results of the search. After a successful search, Siri launches your app so that it can begin the slideshow.

For a list of other intents in the photos domain, see [`INPhotosDomainHandling`](./inphotosdomainhandling.md).

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(dateCreated: INDateComponentsRange?, locationCreated: CLPlacemark?, albumName: String?, searchTerms: [String]?, includedAttributes: INPhotoAttributeOptions, excludedAttributes: INPhotoAttributeOptions, peopleInPhoto: [INPerson]?)](./instartphotoplaybackintent/init%28datecreated,locationcreated,albumname,searchterms,includedattributes,excludedattributes,peopleinphoto%29.md)
  Initializes an intent object with the specified search parameters.
### Getting the People in the Photos
- [var peopleInPhoto: [INPerson]?](./instartphotoplaybackintent/peopleinphoto.md)
  The people in the photos.
- [var peopleInPhotoOperator: INConditionalOperator](./instartphotoplaybackintent/peopleinphotooperator.md)
  The operator that defines how to search for people in the photos.
### Getting the Search Terms
- [var searchTerms: [String]?](./instartphotoplaybackintent/searchterms.md)
  An array of terms to look for in the photos.
- [var searchTermsOperator: INConditionalOperator](./instartphotoplaybackintent/searchtermsoperator.md)
  The operator that defines how to incorporate the search terms when performing the search.
### Getting the Search Attributes
- [var dateCreated: INDateComponentsRange?](./instartphotoplaybackintent/datecreated.md)
  The range of dates during which someone took the pictures.
- [var locationCreated: CLPlacemark?](./instartphotoplaybackintent/locationcreated.md)
  The location where someone took the photos.
- [var albumName: String?](./instartphotoplaybackintent/albumname.md)
  The name of the album that contains the photos.
- [var includedAttributes: INPhotoAttributeOptions](./instartphotoplaybackintent/includedattributes.md)
  The attributes that must be present in the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./instartphotoplaybackintent/excludedattributes.md)
  The attributes that must not be present in the photos.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Photo Playback
- [protocol INStartPhotoPlaybackIntentHandling](./instartphotoplaybackintenthandling.md)
  The handler interface for searching the user’s photos and the playback of the results.
- [class INStartPhotoPlaybackIntentResponse](./instartphotoplaybackintentresponse.md)
  Your app’s response to a start photo playback intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent)*