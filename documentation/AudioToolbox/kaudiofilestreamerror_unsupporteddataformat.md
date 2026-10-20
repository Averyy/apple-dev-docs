# kAudioFileStreamError_UnsupportedDataFormat

**Framework**: Audio Toolbox  
**Kind**: var

The data format is not supported by the specified file type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFileStreamError_UnsupportedDataFormat: OSStatus { get }
```

## See Also

- [Audio File Errors](1576500-audio-file-errors.md)
- [var kAudioFileStreamError_UnsupportedFileType: OSStatus](kaudiofilestreamerror_unsupportedfiletype.md)
  The specified file type is not supported.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_unsupporteddataformat)*