# kAudioFileGlobalInfo_AllExtensions

**Framework**: Audio Toolbox  
**Kind**: var

A `CFArray` of `CFStrings` containing all recognized file extensions. You can use this array when creating an `NSOpenPanel` (declared in the AppKit’s `NSOpenPanel.h` header file).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFileGlobalInfo_AllExtensions: AudioFilePropertyID { get }
```

#### Discussion

If you access this property, your app is responsible for releasing the [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) object.

When accessing this property’s value, you must set the `inSpecifier` parameter to `NULL`.

## See Also

- [var kAudioFileGlobalInfo_ReadableTypes: AudioFilePropertyID](kaudiofileglobalinfo_readabletypes.md)
  An array of `UInt32` values containing the file types (such as AIFF, WAVE, and so forth) that can be opened for reading.
- [var kAudioFileGlobalInfo_WritableTypes: AudioFilePropertyID](kaudiofileglobalinfo_writabletypes.md)
  An array of `UInt32` values containing the file types (such as AIFF, WAVE, and so forth) that can be opened for writing.
- [var kAudioFileGlobalInfo_FileTypeName: AudioFilePropertyID](kaudiofileglobalinfo_filetypename.md)
  The name for the file type.
- [var kAudioFileGlobalInfo_AvailableFormatIDs: AudioFilePropertyID](kaudiofileglobalinfo_availableformatids.md)
  An array of format IDs for formats that can be read.
- [var kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat: AudioFilePropertyID](kaudiofileglobalinfo_availablestreamdescriptionsforformat.md)
  An array of audio stream basic description structures, which contain all the formats for a particular file type and format ID.
- [var kAudioFileGlobalInfo_AllHFSTypeCodes: AudioFilePropertyID](kaudiofileglobalinfo_allhfstypecodes.md)
  An array of HFS type codes containing all recognized HFS type codes. For more information on HFS type codes, see Audio Toolbox’s `ExtendedAudioFile.h` header file.
- [var kAudioFileGlobalInfo_AllUTIs: AudioFilePropertyID](kaudiofileglobalinfo_allutis.md)
  A `CFArray` of `CFString` of all UTIs (Universal Type Identifiers) recognized by Audio File Services.
- [var kAudioFileGlobalInfo_AllMIMETypes: AudioFilePropertyID](kaudiofileglobalinfo_allmimetypes.md)
  A `CFArray` of CF strings of all MIME types are recognized by Audio File Services.
- [var kAudioFileGlobalInfo_ExtensionsForType: AudioFilePropertyID](kaudiofileglobalinfo_extensionsfortype.md)
  A `CFArray` of CF strings containing the recognized file extensions for a specified type.
- [var kAudioFileGlobalInfo_HFSTypeCodesForType: AudioFilePropertyID](kaudiofileglobalinfo_hfstypecodesfortype.md)
  An array of HFS type codes corresponding to a specified file type. The first type in the array is the preferred one to use.
- [var kAudioFileGlobalInfo_UTIsForType: AudioFilePropertyID](kaudiofileglobalinfo_utisfortype.md)
  A `CFArray` of `CFString` of all Universal Type Identifiers recognized by a specified file type.
- [var kAudioFileGlobalInfo_MIMETypesForType: AudioFilePropertyID](kaudiofileglobalinfo_mimetypesfortype.md)
  A `CFArray` of `CFString` of all MIME types recognized by a specified file type.
- [var kAudioFileGlobalInfo_TypesForExtension: AudioFilePropertyID](kaudiofileglobalinfo_typesforextension.md)
  An array of all audio file type IDs that support a specified filename extension.
- [var kAudioFileGlobalInfo_TypesForHFSTypeCode: AudioFilePropertyID](kaudiofileglobalinfo_typesforhfstypecode.md)
  An array of all audio file type IDs that support a specified `HFSTypeCode`.
- [var kAudioFileGlobalInfo_TypesForUTI: AudioFilePropertyID](kaudiofileglobalinfo_typesforuti.md)
  An array of all audio file type IDs that support a specified UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_allextensions)*