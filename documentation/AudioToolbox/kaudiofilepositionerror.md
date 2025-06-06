# kAudioFilePositionError

**Framework**: Audio Toolbox  
**Kind**: var

Invalid file position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFilePositionError: OSStatus { get }
```

## See Also

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
- [var kAudioFileFileNotFoundError: OSStatus](kaudiofilefilenotfounderror.md)
  File not found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepositionerror)*