# Audio File Services

**Framework**: Audio Toolbox

Read or write a variety of audio data to or from disk or a memory buffer.

#### Overview

This document describes Audio File Services, a C programming interface that enables you to read or write a wide variety of audio data to or from disk or a memory buffer.

With Audio File Services you can:

- Create, initialize, open, and close audio files
- Read and write audio files
- Optimize audio files
- Work with user data and global information

## Topics

### Creating and Initializing Audio Files
- [func AudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, AudioFileFlags, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofilecreatewithurl(_:_:_:_:_:).md)
  Creates a new audio file, or initializes an existing file, specified by a URL.
- [func AudioFileInitializeWithCallbacks(UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, AudioFileFlags, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md)
  Deletes the content of an existing file and assigns callbacks to the audio file object.
### Opening and Closing Audio Files
- [func AudioFileOpenURL(CFURL, AudioFilePermissions, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenurl(_:_:_:_:).md)
  Open an existing audio file specified by a URL.
- [func AudioFileOpenWithCallbacks(UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc?, AudioFile_GetSizeProc, AudioFile_SetSizeProc?, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md)
  Opens an existing file with callbacks you provide.
- [func AudioFileClose(AudioFileID) -> OSStatus](audiofileclose(_:).md)
  Closes an audio file.
### Reading and Writing Audio Files
- [func AudioFileReadBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilereadbytes(_:_:_:_:_:).md)
  Reads bytes of audio data from an audio file.
- [func AudioFileWriteBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritebytes(_:_:_:_:_:).md)
  Writes bytes of audio data to an audio file.
- [func AudioFileReadPacketData(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audiofilereadpacketdata(_:_:_:_:_:_:_:).md)
  Reads packets of audio data from an audio file.
- [func AudioFileWritePackets(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritepackets(_:_:_:_:_:_:_:).md)
  Writes packets of audio data to an audio data file.
### Getting and Setting Audio File Properties
- [func AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetproperty(_:_:_:_:).md)
  Gets the value of an audio file property.
- [func AudioFileGetPropertyInfo(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilegetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio file property, including the size of the property value and whether the value is writable.
- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetproperty(_:_:_:_:).md)
  Sets the value of an audio file property
### Working with User Data
- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecountuserdata(_:_:_:).md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilegetuserdatasize(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilegetuserdatasize64(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdata(_:_:_:_:_:).md)
  Gets a chunk from an audio file.
- [func AudioFileGetUserDataAtOffset(AudioFileID, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdataatoffset(_:_:_:_:_:_:).md)
  Gets part of the data from a chunk in an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetuserdata(_:_:_:_:_:).md)
  Sets a user data item in an audio file.
- [func AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus](audiofileremoveuserdata(_:_:_:).md)
  Removes a user data item from an audio file.
### Working with Global Information
- [func AudioFileGetGlobalInfoSize(AudioFilePropertyID, UInt32, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilegetglobalinfosize(_:_:_:_:).md)
  Gets the size of a global audio file property.
- [func AudioFileGetGlobalInfo(AudioFilePropertyID, UInt32, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetglobalinfo(_:_:_:_:_:).md)
  Copies the value of a global property into a buffer.
### Optimizing Audio Files
- [func AudioFileOptimize(AudioFileID) -> OSStatus](audiofileoptimize(_:).md)
  Consolidates audio data and performs other internal optimizations of the file structure.
### Parsing Audio File Content
- [func NextAudioFileRegion(UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](nextaudiofileregion(_:).md)
  Finds the next audio file region in a region list.
- [func NumAudioFileMarkersToNumBytes(Int) -> Int](numaudiofilemarkerstonumbytes(_:).md)
  Returns the number of bytes corresponding to a specified number of audio file markers.
- [func NumBytesToNumAudioFileMarkers(Int) -> Int](numbytestonumaudiofilemarkers(_:).md)
  A macro that returns the number of audio file markers represented by a specified number of bytes.
### Callbacks
- [typealias AudioFile_ReadProc](audiofile_readproc.md)
  Reads audio data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md) functions.)
- [typealias AudioFile_WriteProc](audiofile_writeproc.md)
  A callback for writing file data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md) functions.
- [typealias AudioFile_GetSizeProc](audiofile_getsizeproc.md)
  Gets file data size.
- [typealias AudioFile_SetSizeProc](audiofile_setsizeproc.md)
  Sets file data size.
### Data Types
- [struct AudioBytePacketTranslationFlags](audiobytepackettranslationflags.md)
- [struct AudioFileFlags](audiofileflags.md)
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](audiofilestreamseekflags.md)
- [typealias AudioFileID](audiofileid.md)
  An opaque data type that represents an audio file object.
- [typealias AudioFilePropertyID](audiofilepropertyid.md)
  An audio file property identifier.
- [struct AudioFile_SMPTE_Time](audiofile_smpte_time.md)
  A data structure for describing SMPTE (Society of Motion Picture and Television Engineers) time.
- [struct AudioFileMarker](audiofilemarker.md)
  Annotates a position in an audio file.
- [struct AudioFileMarkerList](audiofilemarkerlist.md)
  A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.
- [struct AudioFileRegion](audiofileregion.md)
  An audio file region specifies a segment of audio data.
- [struct AudioFileRegionList](audiofileregionlist.md)
  A list of the audio file regions in a file.
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.
- [struct AudioFileTypeAndFormatID](audiofiletypeandformatid.md)
  A specifier for the constant[`kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat`](kaudiofileglobalinfo_availablestreamdescriptionsforformat.md).
- [struct AudioIndependentPacketTranslation](audioindependentpackettranslation.md)
- [struct AudioPacketDependencyInfoTranslation](audiopacketdependencyinfotranslation.md)
- [struct AudioPacketRangeByteCountTranslation](audiopacketrangebytecounttranslation.md)
- [struct AudioPacketRollDistanceTranslation](audiopacketrolldistancetranslation.md)
### Enumerations
- [struct AudioBytePacketTranslationFlags](audiobytepackettranslationflags.md)
- [struct AudioFileFlags](audiofileflags.md)
- [enum AudioFilePermissions](audiofilepermissions.md)
  Flags for use when opening an audio file.
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](audiofilestreamseekflags.md)
### Constants
- [typealias AudioFileTypeID](audiofiletypeid.md)
  Operating system constants that indicate the type of file to be written or a hint about what type of file to expect from data provided.
- [Audio File Creation Flags](audio_file_creation_flags.md)
  Flags to set when creating an audio file.
- [enum AudioFilePermissions](audiofilepermissions.md)
  Flags for use when opening an audio file.
- [Audio File Loop Direction Constants](1576494-audio-file-loop-direction-consta.md)
  The playback direction of a looped segment of an audio file.
- [Audio File Marker Types](1576492-audio-file-marker-types.md)
  A type of marker within a file used in the `mType` field of the [`AudioFileMarker`](audiofilemarker.md) structure.
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [Audio File Packet Translation Flags](audio_file_packet_translation_flags.md)
  Flags specified in a packet translation structure.
- [Info String Keys](info-string-keys.md)
  Key values of properties to get and set using Audio File Services functions and provide a common way to get the same information out of several different kinds of files.
- [Audio File Properties](1576499-audio-file-properties.md)
  Properties used by the functions described in getting and setting pieces of data in audio files. See Working with Global Information for details.
- [Audio File Global Info Properties](1576495-audio-file-global-info-propertie.md)
  Access these properties using the functions described in Working with Global Information.
### Result Codes
- [var kAudioFileUnspecifiedError: OSStatus](kaudiofileunspecifiederror.md)
  An unspecified error has occurred.
- [var kAudioFileUnsupportedFileTypeError: OSStatus](kaudiofileunsupportedfiletypeerror.md)
  The file type is not supported.
- [var kAudioFileUnsupportedDataFormatError: OSStatus](kaudiofileunsupporteddataformaterror.md)
  The data format is not supported by this file type.
- [var kAudioFileUnsupportedPropertyError: OSStatus](kaudiofileunsupportedpropertyerror.md)
  The property is not supported.
- [var kAudioFileBadPropertySizeError: OSStatus](kaudiofilebadpropertysizeerror.md)
  The size of the property data was not correct.
- [var kAudioFilePermissionsError: OSStatus](kaudiofilepermissionserror.md)
  The operation violated the file permissions. For example, an attempt was made to write to a file opened with the `kAudioFileReadPermission` constant.
- [var kAudioFileNotOptimizedError: OSStatus](kaudiofilenotoptimizederror.md)
  The chunks following the audio data chunk are preventing the extension of the audio data chunk. To write more data, you must optimize the file.
- [var kAudioFileInvalidChunkError: OSStatus](kaudiofileinvalidchunkerror.md)
  Either the chunk does not exist in the file or it is not supported by the file.
- [var kAudioFileDoesNotAllow64BitDataSizeError: OSStatus](kaudiofiledoesnotallow64bitdatasizeerror.md)
  The file offset was too large for the file type. The AIFF and WAVE file format types have 32-bit file size limits.
- [var kAudioFileInvalidPacketOffsetError: OSStatus](kaudiofileinvalidpacketoffseterror.md)
  A packet offset was past the end of the file, or not at the end of the file when a VBR format was written,  or a corrupt packet size was read when the packet table was built.
- [var kAudioFileInvalidFileError: OSStatus](kaudiofileinvalidfileerror.md)
  The file is malformed, or otherwise not a valid instance of an audio file of its type.
- [var kAudioFileOperationNotSupportedError: OSStatus](kaudiofileoperationnotsupportederror.md)
  The operation cannot be performed.
- [var kAudioFileNotOpenError: OSStatus](kaudiofilenotopenerror.md)
  The file is closed.
- [var kAudioFileEndOfFileError: OSStatus](kaudiofileendoffileerror.md)
  End of file.
- [var kAudioFilePositionError: OSStatus](kaudiofilepositionerror.md)
  Invalid file position.
- [var kAudioFileFileNotFoundError: OSStatus](kaudiofilefilenotfounderror.md)
  File not found.

## See Also

- [Audio Format Services](audio-format-services.md)
  Access information about audio formats and codecs.
- [Extended Audio File Services](extended-audio-file-services.md)
  Read and write compressed files and linear PCM audio files using a simplified interface.
- [Audio File Stream Services](audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Audio File Components](audio-file-components.md)
  Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](core-audio-file-format.md)
  Parse the structure of Core Audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-file-services)*