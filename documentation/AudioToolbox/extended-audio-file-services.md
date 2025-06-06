# Extended Audio File Services

**Framework**: Audio Toolbox

Read and write compressed files and linear PCM audio files using a simplified interface.

#### Overview

Extended Audio File Services provides simplified audio file access, combining features of Audio File Services and Audio Converter Services. It provides a unified interface for reading and writing compressed as well as linear PCM audio files.

## Topics

### Managing Extended Audio File Objects
- [func ExtAudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>?, UInt32, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofilecreatewithurl(_:_:_:_:_:_:).md)
  Creates a new audio file and associates it with a new extended audio file object.
- [func ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus](extaudiofiledispose(_:).md)
  Disposes of an extended audio file object and closes the associated file.
- [func ExtAudioFileOpenURL(CFURL, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofileopenurl(_:_:).md)
  Opens an existing audio file for reading, and associates it with a new extended audio file object.
- [func ExtAudioFileWrapAudioFileID(AudioFileID, Bool, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofilewrapaudiofileid(_:_:_:).md)
  Wraps an audio file object in an extended audio file object.
### Configuring Properties for Extended Audio File Objects
- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](extaudiofilegetproperty(_:_:_:_:).md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](extaudiofilegetpropertyinfo(_:_:_:_:).md)
  Gets information about an extended audio file object property.
- [func ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](extaudiofilesetproperty(_:_:_:_:).md)
  Sets a property value for an extended audio file object.
### Reading and Writing Audio Data
- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](extaudiofileread(_:_:_:).md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](extaudiofileseek(_:_:).md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](extaudiofiletell(_:_:).md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](extaudiofilewrite(_:_:_:).md)
  Performs a synchronous, sequential write operation on an audio file.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](extaudiofilewriteasync(_:_:_:).md)
  Perform an asynchronous, sequential write operation on an audio file.
### Data Types
- [typealias ExtAudioFilePacketTableInfoOverride](extaudiofilepackettableinfooverride.md)
- [typealias ExtAudioFileRef](extaudiofileref.md)
  An opaque structure representing an extended audio file object.
- [typealias ExtAudioFilePropertyID](extaudiofilepropertyid.md)
  An audio file object property identifier.
### Constants
- [Extended Audio FIle Errors](1486883-extended-audio-file-errors.md)
- [Codec Unavailable Errors](1623673-codec-unavailable-errors.md)
- [Property Identifiers for Extended Audio File Objects](1486859-property-identifiers-for-extende.md)
- [Extended Audio File Packet Overrides](3547074-extended-audio-file-packet-overr.md)
### Result Codes
- [var kExtAudioFileError_CodecUnavailableInputConsumed: OSStatus](kextaudiofileerror_codecunavailableinputconsumed.md)
  The [`ExtAudioFileWrite(_:_:_:)`](extaudiofilewrite(_:_:_:).md) function was interrupted and the last buffer that you provided was successfully written to disk.
- [var kExtAudioFileError_CodecUnavailableInputNotConsumed: OSStatus](kextaudiofileerror_codecunavailableinputnotconsumed.md)
  The [`ExtAudioFileWrite(_:_:_:)`](extaudiofilewrite(_:_:_:).md) function was interrupted and the last buffer that you provided was  successfully written to disk.
- [var kExtAudioFileError_InvalidProperty: OSStatus](kextaudiofileerror_invalidproperty.md)
- [var kExtAudioFileError_InvalidPropertySize: OSStatus](kextaudiofileerror_invalidpropertysize.md)
- [var kExtAudioFileError_NonPCMClientFormat: OSStatus](kextaudiofileerror_nonpcmclientformat.md)
- [var kExtAudioFileError_InvalidChannelMap: OSStatus](kextaudiofileerror_invalidchannelmap.md)
  The number of channels does not match the specified format.
- [var kExtAudioFileError_InvalidOperationOrder: OSStatus](kextaudiofileerror_invalidoperationorder.md)
- [var kExtAudioFileError_InvalidDataFormat: OSStatus](kextaudiofileerror_invaliddataformat.md)
- [var kExtAudioFileError_MaxPacketSizeUnknown: OSStatus](kextaudiofileerror_maxpacketsizeunknown.md)
- [var kExtAudioFileError_InvalidSeek: OSStatus](kextaudiofileerror_invalidseek.md)
  An attempt to write, or an offset, is out of bounds.
- [var kExtAudioFileError_AsyncWriteTooLarge: OSStatus](kextaudiofileerror_asyncwritetoolarge.md)
- [var kExtAudioFileError_AsyncWriteBufferOverflow: OSStatus](kextaudiofileerror_asyncwritebufferoverflow.md)
  An asynchronous write operation could not be completed in time.

## See Also

- [Audio Format Services](audio-format-services.md)
  Access information about audio formats and codecs.
- [Audio File Services](audio-file-services.md)
  Read or write a variety of audio data to or from disk or a memory buffer.
- [Audio File Stream Services](audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Audio File Components](audio-file-components.md)
  Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](core-audio-file-format.md)
  Parse the structure of Core Audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extended-audio-file-services)*