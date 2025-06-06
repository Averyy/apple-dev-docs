# iPhoto Media Group Type Identifiers

**Framework**: Media Library

Identifiers for media group types in the iPhoto media source. These constants are used to specify a media group’s [`typeIdentifier`](mlmediagroup/typeidentifier.md) attribute.

## Topics

### Constants
- [let MLiPhotoRootGroupTypeIdentifier: String](mliphotorootgrouptypeidentifier.md)
  The root media group for iPhoto.
- [let MLiPhotoAlbumTypeIdentifier: String](mliphotoalbumtypeidentifier.md)
  A media group that represents an album in iPhoto.
- [let MLiPhotoSmartAlbumTypeIdentifier: String](mliphotosmartalbumtypeidentifier.md)
  A media group that represents a smart album in iPhoto.
- [let MLiPhotoLibraryAlbumTypeIdentifier: String](mliphotolibraryalbumtypeidentifier.md)
  The media group that represents the Photos album in iPhoto.
- [let MLiPhotoFolderAlbumTypeIdentifier: String](mliphotofolderalbumtypeidentifier.md)
  A media group that represents a folder in iPhoto.
- [let MLiPhotoEventAlbumTypeIdentifier: String](mliphotoeventalbumtypeidentifier.md)
  A media group that represents an event in iPhoto.
- [let MLiPhotoEventsFolderTypeIdentifier: String](mliphotoeventsfoldertypeidentifier.md)
  The media group that represents the Events album in iPhoto.
- [let MLiPhotoLastViewedEventAlbumTypeIdentifier: String](mliphotolastviewedeventalbumtypeidentifier.md)
  The media group that represents the last viewed event in iPhoto.
- [let MLiPhotoLastImportAlbumTypeIdentifier: String](mliphotolastimportalbumtypeidentifier.md)
  The media group that represents the Last Import album in iPhoto.
- [let MLiPhotoLastNMonthsAlbumTypeIdentifier: String](mliphotolastnmonthsalbumtypeidentifier.md)
  The media group that represents the recent content album in iPhoto, known as the Last  Months album. The value for  is usually 12 (settable in iPhoto > Preferences > General).
- [let MLiPhotoFlaggedAlbumTypeIdentifier: String](mliphotoflaggedalbumtypeidentifier.md)
  The media group that represents the album of flagged media in iPhoto.
- [let MLiPhotoSubscribedAlbumTypeIdentifier: String](mliphotosubscribedalbumtypeidentifier.md)
  A media group that represents a subscribed album in iPhoto.
- [let MLiPhotoSlideShowAlbumTypeIdentifier: String](mliphotoslideshowalbumtypeidentifier.md)
  A media group that represents a slideshow album in iPhoto.
- [let MLiPhotoPhotoStreamAlbumTypeIdentifier: String](mliphotophotostreamalbumtypeidentifier.md)
  A media group that represents a photo stream in iPhoto.
- [let MLiPhotoFacesAlbumTypeIdentifier: String](mliphotofacesalbumtypeidentifier.md)
  A media group that represents a Faces album in iPhoto. Individual Faces albums are nested in the main Faces album.
- [let MLiPhotoPlacesAlbumTypeIdentifier: String](mliphotoplacesalbumtypeidentifier.md)
  The media group that represents the Places album in iPhoto.
- [let MLiPhotoPlacesCountryAlbumTypeIdentifier: String](mliphotoplacescountryalbumtypeidentifier.md)
  A media group that represents a Places album for a country or region in iPhoto. A country or region album is nested in the main Places album.
- [let MLiPhotoPlacesProvinceAlbumTypeIdentifier: String](mliphotoplacesprovincealbumtypeidentifier.md)
  A media group that represents a Places album for a province or state in iPhoto. A province or state album is nested in a country or region album.
- [let MLiPhotoPlacesCityAlbumTypeIdentifier: String](mliphotoplacescityalbumtypeidentifier.md)
  A media group that represents a Places album for a city in iPhoto. A city album is nested in a province or state album.
- [let MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier: String](mliphotoplacespointofinterestalbumtypeidentifier.md)
  A media group that represents a Places album for a point-of-interest in iPhoto. A point of interest album is nested in a city album.
- [let MLiPhotoFacebookAlbumTypeIdentifier: String](mliphotofacebookalbumtypeidentifier.md)
  A media group that represents a Facebook album that is visible in iPhoto.
- [let MLiPhotoFacebookGroupTypeIdentifier: String](mliphotofacebookgrouptypeidentifier.md)
  A media group that represents a Facebook user account in iPhoto. A Facebook user account contains one or more Facebook albums.
- [let MLiPhotoFlickrAlbumTypeIdentifier: String](mliphotoflickralbumtypeidentifier.md)
  A media group that represents a Flickr album that is visible in iPhoto.
- [let MLiPhotoFlickrGroupTypeIdentifier: String](mliphotoflickrgrouptypeidentifier.md)
  A media group that represents a Flickr user account in iPhoto. A Flickr user account contains one or more Flickr albums.

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

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/iphoto-media-group-type-identifiers)*