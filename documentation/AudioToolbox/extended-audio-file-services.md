# Extended Audio File Services

**Framework**: Audio Toolbox  
**Role**: API Collection

Read and write compressed files and linear PCM audio files using a simplified interface.

#### Overview

Extended Audio File Services provides simplified audio file access, combining features of Audio File Services and Audio Converter Services. It provides a unified interface for reading and writing compressed as well as linear PCM audio files.

## Topics

### Managing Extended Audio File Objects
- [func ExtAudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>?, UInt32, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md)
  Creates a new audio file and associates it with a new extended audio file object.
- [func ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus](./extaudiofiledispose%28_%29.md)
  Disposes of an extended audio file object and closes the associated file.
- [func ExtAudioFileOpenURL(CFURL, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofileopenurl%28_,_%29.md)
  Opens an existing audio file for reading, and associates it with a new extended audio file object.
- [func ExtAudioFileWrapAudioFileID(AudioFileID, Bool, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilewrapaudiofileid%28_,_,_%29.md)
  Wraps an audio file object in an extended audio file object.
### Configuring Properties for Extended Audio File Objects
- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./extaudiofilegetproperty%28_,_,_,_%29.md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./extaudiofilegetpropertyinfo%28_,_,_,_%29.md)
  Gets information about an extended audio file object property.
- [func ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./extaudiofilesetproperty%28_,_,_,_%29.md)
  Sets a property value for an extended audio file object.
### Reading and Writing Audio Data
- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./extaudiofileread%28_,_,_%29.md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](./extaudiofileseek%28_,_%29.md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](./extaudiofiletell%28_,_%29.md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](./extaudiofilewrite%28_,_,_%29.md)
  Performs a synchronous, sequential write operation on an audio file.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](./extaudiofilewriteasync%28_,_,_%29.md)
  Perform an asynchronous, sequential write operation on an audio file.
### Data Types
- [typealias ExtAudioFilePacketTableInfoOverride](./extaudiofilepackettableinfooverride.md)
- [typealias ExtAudioFileRef](./extaudiofileref.md)
  An opaque structure representing an extended audio file object.
- [typealias ExtAudioFilePropertyID](./extaudiofilepropertyid.md)
  An audio file object property identifier.
### Constants
- [Extended Audio FIle Errors](./api-1486883-extended-audio-file-errors.md)
- [Codec Unavailable Errors](./api-1623673-codec-unavailable-errors.md)
- [Property Identifiers for Extended Audio File Objects](./api-1486859-property-identifiers-for-extende.md)
- [Extended Audio File Packet Overrides](./api-3547074-extended-audio-file-packet-overr.md)
### Result Codes
- [var kExtAudioFileError_CodecUnavailableInputConsumed: OSStatus](./kextaudiofileerror_codecunavailableinputconsumed.md)
  The [`ExtAudioFileWrite(_:_:_:)`](./extaudiofilewrite%28_,_,_%29.md) function was interrupted and the last buffer that you provided was successfully written to disk.
- [var kExtAudioFileError_CodecUnavailableInputNotConsumed: OSStatus](./kextaudiofileerror_codecunavailableinputnotconsumed.md)
  The [`ExtAudioFileWrite(_:_:_:)`](./extaudiofilewrite%28_,_,_%29.md) function was interrupted and the last buffer that you provided was *not* successfully written to disk.
- [var kExtAudioFileError_InvalidProperty: OSStatus](./kextaudiofileerror_invalidproperty.md)
- [var kExtAudioFileError_InvalidPropertySize: OSStatus](./kextaudiofileerror_invalidpropertysize.md)
- [var kExtAudioFileError_NonPCMClientFormat: OSStatus](./kextaudiofileerror_nonpcmclientformat.md)
- [var kExtAudioFileError_InvalidChannelMap: OSStatus](./kextaudiofileerror_invalidchannelmap.md)
  The number of channels does not match the specified format.
- [var kExtAudioFileError_InvalidOperationOrder: OSStatus](./kextaudiofileerror_invalidoperationorder.md)
- [var kExtAudioFileError_InvalidDataFormat: OSStatus](./kextaudiofileerror_invaliddataformat.md)
- [var kExtAudioFileError_MaxPacketSizeUnknown: OSStatus](./kextaudiofileerror_maxpacketsizeunknown.md)
- [var kExtAudioFileError_InvalidSeek: OSStatus](./kextaudiofileerror_invalidseek.md)
  An attempt to write, or an offset, is out of bounds.
- [var kExtAudioFileError_AsyncWriteTooLarge: OSStatus](./kextaudiofileerror_asyncwritetoolarge.md)
- [var kExtAudioFileError_AsyncWriteBufferOverflow: OSStatus](./kextaudiofileerror_asyncwritebufferoverflow.md)
  An asynchronous write operation could not be completed in time.
### Deprecated Functions
- [ExtAudioFileCreateNew](./extaudiofilecreatenew.md)
  Deprecated. Use the [`ExtAudioFileCreateWithURL`](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md) function instead.
- [ExtAudioFileOpen](./extaudiofileopen.md)
  Deprecated. Use the [`ExtAudioFileOpenURL`](./extaudiofileopenurl%28_,_%29.md) function instead.

## See Also

### Audio Files and Formats
- [Audio Format Services](./audio-format-services.md)
  Access information about audio formats and codecs.
- [Audio File Services](./audio-file-services.md)
  Read or write a variety of audio data to or from disk or a memory buffer.
- [Audio File Stream Services](./audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Audio File Components](./audio-file-components.md)
  Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](./core-audio-file-format.md)
  Parse the structure of Core Audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extended-audio-file-services)*