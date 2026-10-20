# MLMediaObjectChannelCountKey

**Framework**: Media Library  
**Kind**: var  
**Role**: Global Variable

Specifies the media object’s channel count. The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
let MLMediaObjectChannelCountKey: String
```

```c
extern NSString * const MLMediaObjectChannelCountKey;
```

## See Also

### Constants
- [let MLMediaObjectDurationKey: String](./mlmediaobjectdurationkey.md)
  Specifies the media object’s duration, in seconds. The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)).
- [let MLMediaObjectArtistKey: String](./mlmediaobjectartistkey.md)
  Specifies the media object’s artist. The value for this key is a string ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectAlbumKey: String](./mlmediaobjectalbumkey.md)
  Specifies the media object’s album. The value for this key is a string ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectGenreKey: String](./mlmediaobjectgenrekey.md)
  Specifies the media object’s genre. The value for this key is a string ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectKindKey: String](./mlmediaobjectkindkey.md)
  Used by iTunes only. Specifies the media object’s file format (shown in the “Kind” column in iTunes). The value for this key is a string ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectTrackNumberKey: String](./mlmediaobjecttracknumberkey.md)
  Specifies the media object’s track number. The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)).
- [let MLMediaObjectBitRateKey: String](./mlmediaobjectbitratekey.md)
  Specifies the media object’s bit rate, in kilobits per second. The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)).
- [let MLMediaObjectSampleRateKey: String](./mlmediaobjectsampleratekey.md)
  Specifies the media object’s sample rate, in samples per second (Hz). The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)).
- [let MLMediaObjectResolutionStringKey: String](./mlmediaobjectresolutionstringkey.md)
  Specifies the media object’s resolution. The value for this key is a string ([`NSString`](../Foundation/nsstring.md)) intended to be converted to a size ([`NSSize`](../Foundation/nssize.md)) using the [`NSSizeFromString(_:)`](../Foundation/nssizefromstring%28_%29.md) method.
- [let MLMediaObjectCommentsKey: String](./mlmediaobjectcommentskey.md)
  Specifies the contents of the comments field associated with the media object. The value for this key is a string ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectKeywordsKey: String](./mlmediaobjectkeywordskey.md)
  Specifies the keywords associated with the media object. The value for this key is an array ([`NSArray`](../Foundation/nsarray.md)) of strings ([`NSString`](../Foundation/nsstring.md)).
- [let MLMediaObjectProtectedKey: String](./mlmediaobjectprotectedkey.md)
  Specifies whether the media object is protected by DRM (Digital Rights Management). The value for this key is a number ([`NSNumber`](../Foundation/nsnumber.md)), 0 or 1, that represents a Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobjectchannelcountkey)*