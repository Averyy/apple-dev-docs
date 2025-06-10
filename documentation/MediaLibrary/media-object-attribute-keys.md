# Media Object Attribute Keys

**Framework**: Media Library

Attribute keys for a media object. These constants are used to specify keys within a media object’s [`attributes`](mlmediaobject/attributes.md) dictionary.

## Topics

### Constants
- [let MLMediaObjectDurationKey: String](mlmediaobjectdurationkey.md)
  Specifies the media object’s duration, in seconds. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)).
- [let MLMediaObjectArtistKey: String](mlmediaobjectartistkey.md)
  Specifies the media object’s artist. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectAlbumKey: String](mlmediaobjectalbumkey.md)
  Specifies the media object’s album. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectGenreKey: String](mlmediaobjectgenrekey.md)
  Specifies the media object’s genre. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectKindKey: String](mlmediaobjectkindkey.md)
  Used by iTunes only. Specifies the media object’s file format (shown in the “Kind” column in iTunes). The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectTrackNumberKey: String](mlmediaobjecttracknumberkey.md)
  Specifies the media object’s track number. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)).
- [let MLMediaObjectBitRateKey: String](mlmediaobjectbitratekey.md)
  Specifies the media object’s bit rate, in kilobits per second. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)).
- [let MLMediaObjectSampleRateKey: String](mlmediaobjectsampleratekey.md)
  Specifies the media object’s sample rate, in samples per second (Hz). The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)).
- [let MLMediaObjectChannelCountKey: String](mlmediaobjectchannelcountkey.md)
  Specifies the media object’s channel count. The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)).
- [let MLMediaObjectResolutionStringKey: String](mlmediaobjectresolutionstringkey.md)
  Specifies the media object’s resolution. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)) intended to be converted to a size ([`NSSize`](https://developer.apple.com/documentation/Foundation/NSSize)) using the [`NSSizeFromString(_:)`](https://developer.apple.com/documentation/Foundation/NSSizeFromString(_:)) method.
- [let MLMediaObjectCommentsKey: String](mlmediaobjectcommentskey.md)
  Specifies the contents of the comments field associated with the media object. The value for this key is a string ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectKeywordsKey: String](mlmediaobjectkeywordskey.md)
  Specifies the keywords associated with the media object. The value for this key is an array ([`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray)) of strings ([`NSString`](https://developer.apple.com/documentation/Foundation/NSString)).
- [let MLMediaObjectProtectedKey: String](mlmediaobjectprotectedkey.md)
  Specifies whether the media object is protected by DRM (Digital Rights Management). The value for this key is a number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)), 0 or 1, that represents a Boolean value.

## See Also

- [Aperture Media Group Type Identifiers](aperture-media-group-type-identifiers.md)
  Identifiers for media group types in the Aperture media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [Final Cut Pro Media Group Type Identifiers](final-cut-pro-media-group-type-identifiers.md)
  Identifiers for media group types in the Final Cut Pro media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [Folders Media Group Type Identifiers](folders-media-group-type-identifiers.md)
  Identifiers for media group types in folder-based media sources. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [GarageBand Media Group Type Identifiers](garageband-media-group-type-identifiers.md)
  Identifiers for media group types in the GarageBand media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [Logic Media Group Type Identifiers](logic-media-group-type-identifiers.md)
  Identifiers for media group types in the Logic media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [let MLMediaLoadAppFoldersKey: String](mlmedialoadappfolderskey.md)
  Specifies one or more relative paths inside the caller’s app bundle in which to search for media files. The value for this key is an array of strings (relative paths inside the caller’s app bundle).
- [let MLMediaLoadAppleLoops: String](mlmedialoadappleloops.md)
  Identifies the folder containing audio loops from Apple.
- [let MLMediaLoadExcludeSourcesKey: String](mlmedialoadexcludesourceskey.md)
  Defines which media sources to exclude when loading. This option is processed after [`MLMediaLoadIncludeSourcesKey`](mlmedialoadincludesourceskey.md). The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [`Media Source Identifiers`](media-source-identifiers.md).
- [let MLMediaLoadFoldersKey: String](mlmedialoadfolderskey.md)
  Specifies the well-known folders that should be searched for media files. If this key is not present, none of the well-known folders will be provided. The value for this key is an array of strings (identifiers that correspond to well-known folder locations). For a list of well-known folder identifiers, see [`Well-Known Folder Identifiers`](well-known-folder-identifiers.md).
- [let MLMediaLoadIncludeSourcesKey: String](mlmedialoadincludesourceskey.md)
  Defines which media sources to include when loading. If not present, load all available media sources. This option is processed after [`MLMediaLoadSourceTypesKey`](mlmedialoadsourcetypeskey.md). If [`MLMediaLoadIncludeSourcesKey`](mlmedialoadincludesourceskey.md) is present but [`MLMediaLoadSourceTypesKey`](mlmedialoadsourcetypeskey.md) is not, then only those sources specified here will be loaded. This is useful for loading a single media source. When both keys are present, this is useful for adding one or more media sources that normally would not appear for the requested library type. The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [`Media Source Identifiers`](media-source-identifiers.md).
- [let MLMediaLoadMoviesFolder: String](mlmedialoadmoviesfolder.md)
  Identifies the user’s Movies folder.
- [let MLMediaLoadSourceTypesKey: String](mlmedialoadsourcetypeskey.md)
  Defines which sources to load based on library type. If not present, this will load all sources. The value for this key is a media source type. For a list of valid media source types, see [`MLMediaSourceType`](mlmediasourcetype.md).
- [let MLMediaSourceApertureIdentifier: String](mlmediasourceapertureidentifier.md)
  The media source providing content from Aperture.
- [let MLMediaSourceAppDefinedFoldersIdentifier: String](mlmediasourceappdefinedfoldersidentifier.md)
  The media source for app-defined folders. This identifies a media source created from a relative path inside the caller’s app bundle. This source provides data when [`MLMediaLoadAppFoldersKey`](mlmedialoadappfolderskey.md) is provided in the options.
- [let MLMediaSourceCustomFoldersIdentifier: String](mlmediasourcecustomfoldersidentifier.md)
  The media source for custom folders. Currently, the only custom folder is the folder containing audio loops from Apple. This source provides data when [`MLMediaLoadFoldersKey`](mlmedialoadfolderskey.md) is provided with the [`MLMediaLoadAppleLoops`](mlmedialoadappleloops.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/media-object-attribute-keys)*