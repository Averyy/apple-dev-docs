# Audio File Errors

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kAudioFileBadPropertySizeError: OSStatus](kaudiofilebadpropertysizeerror.md)
  The size of the property data was not correct.
- [var kAudioFileDoesNotAllow64BitDataSizeError: OSStatus](kaudiofiledoesnotallow64bitdatasizeerror.md)
  The file offset was too large for the file type. The AIFF and WAVE file format types have 32-bit file size limits.
- [var kAudioFileEndOfFileError: OSStatus](kaudiofileendoffileerror.md)
  End of file.
- [var kAudioFileFileNotFoundError: OSStatus](kaudiofilefilenotfounderror.md)
  File not found.
- [var kAudioFileInvalidChunkError: OSStatus](kaudiofileinvalidchunkerror.md)
  Either the chunk does not exist in the file or it is not supported by the file.
- [var kAudioFileInvalidFileError: OSStatus](kaudiofileinvalidfileerror.md)
  The file is malformed, or otherwise not a valid instance of an audio file of its type.
- [var kAudioFileInvalidPacketOffsetError: OSStatus](kaudiofileinvalidpacketoffseterror.md)
  A packet offset was past the end of the file, or not at the end of the file when a VBR format was written,  or a corrupt packet size was read when the packet table was built.
- [var kAudioFileNotOpenError: OSStatus](kaudiofilenotopenerror.md)
  The file is closed.
- [var kAudioFileNotOptimizedError: OSStatus](kaudiofilenotoptimizederror.md)
  The chunks following the audio data chunk are preventing the extension of the audio data chunk. To write more data, you must optimize the file.
- [var kAudioFileOperationNotSupportedError: OSStatus](kaudiofileoperationnotsupportederror.md)
  The operation cannot be performed.
- [var kAudioFilePermissionsError: OSStatus](kaudiofilepermissionserror.md)
  The operation violated the file permissions. For example, an attempt was made to write to a file opened with the `kAudioFileReadPermission` constant.
- [var kAudioFilePositionError: OSStatus](kaudiofilepositionerror.md)
  Invalid file position.
- [var kAudioFileUnspecifiedError: OSStatus](kaudiofileunspecifiederror.md)
  An unspecified error has occurred.
- [var kAudioFileUnsupportedDataFormatError: OSStatus](kaudiofileunsupporteddataformaterror.md)
  The data format is not supported by this file type.
- [var kAudioFileUnsupportedFileTypeError: OSStatus](kaudiofileunsupportedfiletypeerror.md)
  The file type is not supported.
- [var kAudioFileUnsupportedPropertyError: OSStatus](kaudiofileunsupportedpropertyerror.md)
  The property is not supported.
- [var kAudioFileInvalidPacketDependencyError: OSStatus](kaudiofileinvalidpacketdependencyerror.md)

## See Also

- [var kAudioFileStreamError_UnsupportedFileType: OSStatus](kaudiofilestreamerror_unsupportedfiletype.md)
  The specified file type is not supported.
- [var kAudioFileStreamError_UnsupportedDataFormat: OSStatus](kaudiofilestreamerror_unsupporteddataformat.md)
  The data format is not supported by the specified file type.
- [var kAudioFileStreamError_UnsupportedProperty: OSStatus](kaudiofilestreamerror_unsupportedproperty.md)
  The property is not supported.
- [var kAudioFileStreamError_BadPropertySize: OSStatus](kaudiofilestreamerror_badpropertysize.md)
  The size of the buffer you provided for property data was not correct.
- [var kAudioFileStreamError_NotOptimized: OSStatus](kaudiofilestreamerror_notoptimized.md)
  It is not possible to produce output packets because the streamed audio file’s packet table or other defining information is not present or appears after the audio data.
- [var kAudioFileStreamError_InvalidPacketOffset: OSStatus](kaudiofilestreamerror_invalidpacketoffset.md)
  A packet offset was less than `0`, or past the end of the file, or a corrupt packet size was read when building the packet table.
- [var kAudioFileStreamError_InvalidFile: OSStatus](kaudiofilestreamerror_invalidfile.md)
  The file is malformed, not a valid instance of an audio file of its type, or not recognized as an audio file.
- [var kAudioFileStreamError_ValueUnknown: OSStatus](kaudiofilestreamerror_valueunknown.md)
  The property value is not present in this file before the audio data.
- [var kAudioFileStreamError_DataUnavailable: OSStatus](kaudiofilestreamerror_dataunavailable.md)
  The amount of data provided to the parser was insufficient to produce any result.
- [var kAudioFileStreamError_IllegalOperation: OSStatus](kaudiofilestreamerror_illegaloperation.md)
  An illegal operation was attempted.
- [var kAudioFileStreamError_UnspecifiedError: OSStatus](kaudiofilestreamerror_unspecifiederror.md)
  An unspecified error has occurred.
- [var kAudioFileStreamError_DiscontinuityCantRecover: OSStatus](kaudiofilestreamerror_discontinuitycantrecover.md)
  A discontinuity has occurred in the audio data, and Audio File Stream Services cannot recover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1576500-audio-file-errors)*