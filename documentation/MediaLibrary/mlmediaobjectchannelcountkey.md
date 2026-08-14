# MLMediaObjectChannelCountKey

**Framework**: Media Library  
**Kind**: var

Specifies the media object’s channel count. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
let MLMediaObjectChannelCountKey: String
```

## See Also

- [let MLMediaObjectDurationKey: String](mlmediaobjectdurationkey.md)
  Specifies the media object’s duration, in seconds. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)).
- [let MLMediaObjectArtistKey: String](mlmediaobjectartistkey.md)
  Specifies the media object’s artist. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectAlbumKey: String](mlmediaobjectalbumkey.md)
  Specifies the media object’s album. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectGenreKey: String](mlmediaobjectgenrekey.md)
  Specifies the media object’s genre. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectKindKey: String](mlmediaobjectkindkey.md)
  Used by iTunes only. Specifies the media object’s file format (shown in the “Kind” column in iTunes). The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectTrackNumberKey: String](mlmediaobjecttracknumberkey.md)
  Specifies the media object’s track number. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)).
- [let MLMediaObjectBitRateKey: String](mlmediaobjectbitratekey.md)
  Specifies the media object’s bit rate, in kilobits per second. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)).
- [let MLMediaObjectSampleRateKey: String](mlmediaobjectsampleratekey.md)
  Specifies the media object’s sample rate, in samples per second (Hz). The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)).
- [let MLMediaObjectResolutionStringKey: String](mlmediaobjectresolutionstringkey.md)
  Specifies the media object’s resolution. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)) intended to be converted to a size ([`NSSize`](https://developer.apple.com/documentation/foundation/nssize)) using the [`NSSizeFromString(_:)`](https://developer.apple.com/documentation/foundation/nssizefromstring(_:)) method.
- [let MLMediaObjectCommentsKey: String](mlmediaobjectcommentskey.md)
  Specifies the contents of the comments field associated with the media object. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectKeywordsKey: String](mlmediaobjectkeywordskey.md)
  Specifies the keywords associated with the media object. The value for this key is an array ([`NSArray`](https://developer.apple.com/documentation/foundation/nsarray)) of strings ([`NSString`](https://developer.apple.com/documentation/foundation/nsstring)).
- [let MLMediaObjectProtectedKey: String](mlmediaobjectprotectedkey.md)
  Specifies whether the media object is protected by DRM (Digital Rights Management). The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)), 0 or 1, that represents a Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobjectchannelcountkey)*