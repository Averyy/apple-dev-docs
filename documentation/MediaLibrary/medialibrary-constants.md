# MediaLibrary Constants

**Framework**: Media Library

## Topics

### Constants
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
- [let MLMediaSourceFinalCutIdentifier: String](mlmediasourcefinalcutidentifier.md)
  The media source providing content from Final Cut Pro.
- [let MLMediaSourceGarageBandIdentifier: String](mlmediasourcegaragebandidentifier.md)
  The media source providing content from GarageBand.
- [let MLMediaSourceLogicIdentifier: String](mlmediasourcelogicidentifier.md)
  The media source providing content from Logic.
- [let MLMediaSourceMoviesFolderIdentifier: String](mlmediasourcemoviesfolderidentifier.md)
  The media source for the user’s Movies folder. This source provides data when [`MLMediaLoadFoldersKey`](mlmedialoadfolderskey.md) is provided with the [`MLMediaLoadMoviesFolder`](mlmedialoadmoviesfolder.md) value.
- [let MLMediaSourcePhotoBoothIdentifier: String](mlmediasourcephotoboothidentifier.md)
  The media source providing content from Photo Booth.
- [let MLMediaSourcePhotosIdentifier: String](mlmediasourcephotosidentifier.md)
- [struct MLMediaSourceType](mlmediasourcetype.md)
  Specifies the source type associated with a particular media source. Source type reflects the primary type of media within the source. These constants are used to specify values for [`MLMediaLoadSourceTypesKey`](mlmedialoadsourcetypeskey.md) in the [`init(options:)`](mlmedialibrary/init(options:).md) method of [`MLMediaLibrary`](mlmedialibrary.md).
- [let MLMediaSourceiMovieIdentifier: String](mlmediasourceimovieidentifier.md)
  The media source providing content from iMovie.
- [let MLMediaSourceiPhotoIdentifier: String](mlmediasourceiphotoidentifier.md)
  The media source providing content from iPhoto.
- [let MLMediaSourceiTunesIdentifier: String](mlmediasourceitunesidentifier.md)
  The media source providing content from iTunes.
- [enum MLMediaType](mlmediatype.md)
  Specifies the media type associated with a particular media object. These constants are used to specify a media object’s [`mediaType`](mlmediaobject/mediatype.md) attribute.
- [let MLPhotosAlbumTypeIdentifier: String](mlphotosalbumtypeidentifier.md)
- [let MLPhotosAlbumsGroupTypeIdentifier: String](mlphotosalbumsgrouptypeidentifier.md)
- [let MLPhotosAllCollectionsGroupTypeIdentifier: String](mlphotosallcollectionsgrouptypeidentifier.md)
- [let MLPhotosAllMomentsGroupTypeIdentifier: String](mlphotosallmomentsgrouptypeidentifier.md)
- [let MLPhotosAllPhotosAlbumTypeIdentifier: String](mlphotosallphotosalbumtypeidentifier.md)
- [let MLPhotosAllYearsGroupTypeIdentifier: String](mlphotosallyearsgrouptypeidentifier.md)
- [let MLPhotosBurstGroupTypeIdentifier: String](mlphotosburstgrouptypeidentifier.md)
- [let MLPhotosCollectionGroupTypeIdentifier: String](mlphotoscollectiongrouptypeidentifier.md)
- [let MLPhotosDepthEffectGroupTypeIdentifier: String](mlphotosdeptheffectgrouptypeidentifier.md)
- [let MLPhotosFacesAlbumTypeIdentifier: String](mlphotosfacesalbumtypeidentifier.md)
- [let MLPhotosFavoritesGroupTypeIdentifier: String](mlphotosfavoritesgrouptypeidentifier.md)
- [let MLPhotosFolderTypeIdentifier: String](mlphotosfoldertypeidentifier.md)
- [let MLPhotosFrontCameraGroupTypeIdentifier: String](mlphotosfrontcameragrouptypeidentifier.md)
- [let MLPhotosLastImportGroupTypeIdentifier: String](mlphotoslastimportgrouptypeidentifier.md)
- [let MLPhotosMomentGroupTypeIdentifier: String](mlphotosmomentgrouptypeidentifier.md)
- [let MLPhotosMyPhotoStreamTypeIdentifier: String](mlphotosmyphotostreamtypeidentifier.md)
- [let MLPhotosPanoramasGroupTypeIdentifier: String](mlphotospanoramasgrouptypeidentifier.md)
- [let MLPhotosPublishedAlbumTypeIdentifier: String](mlphotospublishedalbumtypeidentifier.md)
- [let MLPhotosRootGroupTypeIdentifier: String](mlphotosrootgrouptypeidentifier.md)
- [let MLPhotosScreenshotGroupTypeIdentifier: String](mlphotosscreenshotgrouptypeidentifier.md)
- [let MLPhotosSharedGroupTypeIdentifier: String](mlphotossharedgrouptypeidentifier.md)
- [let MLPhotosSharedPhotoStreamTypeIdentifier: String](mlphotossharedphotostreamtypeidentifier.md)
- [let MLPhotosSloMoGroupTypeIdentifier: String](mlphotosslomogrouptypeidentifier.md)
- [let MLPhotosSmartAlbumTypeIdentifier: String](mlphotossmartalbumtypeidentifier.md)
- [let MLPhotosTimelapseGroupTypeIdentifier: String](mlphotostimelapsegrouptypeidentifier.md)
- [let MLPhotosVideosGroupTypeIdentifier: String](mlphotosvideosgrouptypeidentifier.md)
- [let MLPhotosYearGroupTypeIdentifier: String](mlphotosyeargrouptypeidentifier.md)
- [let MLiTunesMusicVideosPlaylistTypeIdentifier: String](mlitunesmusicvideosplaylisttypeidentifier.md)
- [let MLiTunesVideoPlaylistTypeIdentifier: String](mlitunesvideoplaylisttypeidentifier.md)
- [Media Object Attribute Keys](media-object-attribute-keys.md)
  Attribute keys for a media object. These constants are used to specify keys within a media object’s [`attributes`](mlmediaobject/attributes.md) dictionary.
- [iMovie Media Group Type Identifiers](imovie-media-group-type-identifiers.md)
  Identifiers for media group types in the iMovie media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [iPhoto Media Group Type Identifiers](iphoto-media-group-type-identifiers.md)
  Identifiers for media group types in the iPhoto media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [iTunes Media Group Type Identifiers](itunes-media-group-type-identifiers.md)
  Identifiers for media group types in the iTunes media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.
- [let MLPhotosAnimatedGroupTypeIdentifier: String](mlphotosanimatedgrouptypeidentifier.md)
- [let MLPhotosLivePhotosGroupTypeIdentifier: String](mlphotoslivephotosgrouptypeidentifier.md)
- [let MLPhotosLongExposureGroupTypeIdentifier: String](mlphotoslongexposuregrouptypeidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/medialibrary-constants)*