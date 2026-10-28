# INSearchForPhotosIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the list of photos that match the specified criteria.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchForPhotosIntent
```

```objc
@interface INSearchForPhotosIntent : INIntent
```

## Overview

The system creates an [`INSearchForPhotosIntent`](./insearchforphotosintent.md) object when the user asks to search for photos in an app. The intent object contains the parameters to use during the search, including the possible name of a photo album, the people in the photos, or the location of the photos. Use this intent object to validate the search parameters and to begin the search process. When performing the search, use only the provided parameters and ignore any that have no values.

To handle this intent, the handler object in your Intents extension must adopt the [`INSearchForPhotosIntentHandling`](./insearchforphotosintenthandling.md) protocol. Your handler should confirm the request and create an [`INSearchForPhotosIntentResponse`](./insearchforphotosintentresponse.md) object with the results of the search. For successful searches, Siri offers the user a way to launch your app and see the results.

For a list of other intents in the photos domain, see [`INPhotosDomainHandling`](./inphotosdomainhandling.md).

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(dateCreated: INDateComponentsRange?, locationCreated: CLPlacemark?, albumName: String?, searchTerms: [String]?, includedAttributes: INPhotoAttributeOptions, excludedAttributes: INPhotoAttributeOptions, peopleInPhoto: [INPerson]?)](./insearchforphotosintent/init%28datecreated,locationcreated,albumname,searchterms,includedattributes,excludedattributes,peopleinphoto%29.md)
  Initializes a search for photos intent object with the specified search parameters.
### Getting the People in the Photos
- [var peopleInPhoto: [INPerson]?](./insearchforphotosintent/peopleinphoto.md)
  The people identified in the photos.
- [var peopleInPhotoOperator: INConditionalOperator](./insearchforphotosintent/peopleinphotooperator.md)
  The operator that defines how to search for people in the photos.
### Getting the Search Terms
- [var searchTerms: [String]?](./insearchforphotosintent/searchterms.md)
  An array of terms to look for in the photos.
- [var searchTermsOperator: INConditionalOperator](./insearchforphotosintent/searchtermsoperator.md)
  The operator that defines how to incorporate the search terms when performing the search.
### Getting the Search Attributes
- [var dateCreated: INDateComponentsRange?](./insearchforphotosintent/datecreated.md)
  The range of dates during which someone took the pictures.
- [var locationCreated: CLPlacemark?](./insearchforphotosintent/locationcreated.md)
  The location where someone took the photos.
- [var albumName: String?](./insearchforphotosintent/albumname.md)
  The name of the album that contains the photos.
- [var includedAttributes: INPhotoAttributeOptions](./insearchforphotosintent/includedattributes.md)
  The attributes that must be present in the photos.
- [var excludedAttributes: INPhotoAttributeOptions](./insearchforphotosintent/excludedattributes.md)
  The attributes that must not be present in the photos.
- [struct INPhotoAttributeOptions](./inphotoattributeoptions.md)
  Constants indicating attributes of a photo.

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

### Photo Search
- [protocol INSearchForPhotosIntentHandling](./insearchforphotosintenthandling.md)
  The handler interface for searching the user’s photos.
- [class INSearchForPhotosIntentResponse](./insearchforphotosintentresponse.md)
  Your app’s response to a search for photos intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintent)*