# Load Options Keys

**Framework**: Media Library

Keys used to specify the `options` dictionary argument to [`init(options:)`](mlmedialibrary/init(options:).md).

## Topics

### Constants
- [let MLMediaLoadSourceTypesKey: String](mlmedialoadsourcetypeskey.md)
  Defines which sources to load based on library type. If not present, this will load all sources. The value for this key is a media source type. For a list of valid media source types, see [`MLMediaSourceType`](mlmediasourcetype.md).
- [let MLMediaLoadIncludeSourcesKey: String](mlmedialoadincludesourceskey.md)
  Defines which media sources to include when loading. If not present, load all available media sources. This option is processed after [`MLMediaLoadSourceTypesKey`](mlmedialoadsourcetypeskey.md). If [`MLMediaLoadIncludeSourcesKey`](mlmedialoadincludesourceskey.md) is present but [`MLMediaLoadSourceTypesKey`](mlmedialoadsourcetypeskey.md) is not, then only those sources specified here will be loaded. This is useful for loading a single media source. When both keys are present, this is useful for adding one or more media sources that normally would not appear for the requested library type. The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [`Media Source Identifiers`](media-source-identifiers.md).
- [let MLMediaLoadExcludeSourcesKey: String](mlmedialoadexcludesourceskey.md)
  Defines which media sources to exclude when loading. This option is processed after [`MLMediaLoadIncludeSourcesKey`](mlmedialoadincludesourceskey.md). The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [`Media Source Identifiers`](media-source-identifiers.md).
- [let MLMediaLoadFoldersKey: String](mlmedialoadfolderskey.md)
  Specifies the well-known folders that should be searched for media files. If this key is not present, none of the well-known folders will be provided. The value for this key is an array of strings (identifiers that correspond to well-known folder locations). For a list of well-known folder identifiers, see [`Well-Known Folder Identifiers`](well-known-folder-identifiers.md).
- [let MLMediaLoadAppFoldersKey: String](mlmedialoadappfolderskey.md)
  Specifies one or more relative paths inside the caller’s app bundle in which to search for media files. The value for this key is an array of strings (relative paths inside the caller’s app bundle).

## See Also

- [Media Source Identifiers](media-source-identifiers.md)
  Identifiers for media sources which correspond to apps used to manage groups of media objects. Used with [`Load Options Keys`](load-options-keys.md).
- [Non-App-Specific Media Source Identifiers](non-app-specific-media-source-identifiers.md)
  Identifiers for media sources which do not correspond to apps. Used with [`Load Options Keys`](load-options-keys.md).
- [Well-Known Folder Identifiers](well-known-folder-identifiers.md)
  Identifiers for well-known media folders used to specify the value for [`MLMediaLoadFoldersKey`](mlmedialoadfolderskey.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/load-options-keys)*