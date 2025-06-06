# kExtAudioFileProperty_ClientMaxPacketSize

**Framework**: Audio Toolbox  
**Kind**: var

Your application audio data format’s maximum packet size, in bytes. Value is a read-only `UInt32`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kExtAudioFileProperty_ClientMaxPacketSize: ExtAudioFilePropertyID { get }
```

## See Also

- [var kExtAudioFileProperty_FileDataFormat: ExtAudioFilePropertyID](kextaudiofileproperty_filedataformat.md)
  A file’s data format.
- [var kExtAudioFileProperty_FileChannelLayout: ExtAudioFilePropertyID](kextaudiofileproperty_filechannellayout.md)
  A file’s channel layout.
- [var kExtAudioFileProperty_ClientDataFormat: ExtAudioFilePropertyID](kextaudiofileproperty_clientdataformat.md)
  The audio stream format for your application.
- [var kExtAudioFileProperty_ClientChannelLayout: ExtAudioFilePropertyID](kextaudiofileproperty_clientchannellayout.md)
  The audio channel layout for your application.
- [var kExtAudioFileProperty_CodecManufacturer: ExtAudioFilePropertyID](kextaudiofileproperty_codecmanufacturer.md)
  The manufacturer of the codec to be used by the extended audio file object. Value is a read/write `UInt32`.
- [var kExtAudioFileProperty_AudioConverter: ExtAudioFilePropertyID](kextaudiofileproperty_audioconverter.md)
  The audio converter object associated with the extended audio file object, if a converter is associated.
- [var kExtAudioFileProperty_AudioFile: ExtAudioFilePropertyID](kextaudiofileproperty_audiofile.md)
  The audio file object associated with the extended audio file object.
- [var kExtAudioFileProperty_FileMaxPacketSize: ExtAudioFilePropertyID](kextaudiofileproperty_filemaxpacketsize.md)
  The file data format’s maximum packet size, in bytes. Value is a read-only `UInt32`.
- [var kExtAudioFileProperty_FileLengthFrames: ExtAudioFilePropertyID](kextaudiofileproperty_filelengthframes.md)
  The associated audio file’s length in sample frames. Value is an `SInt64`. For a PCM file, the value is read/write. For a non-PCM file, the value is read-only.
- [var kExtAudioFileProperty_ConverterConfig: ExtAudioFilePropertyID](kextaudiofileproperty_converterconfig.md)
  The configuration of the extended audio file object’s associated audio converter, as specified by the `kAudioConverterPropertySettings` property. Value is a read/write `CFArray` object.
- [var kExtAudioFileProperty_IOBufferSizeBytes: ExtAudioFilePropertyID](kextaudiofileproperty_iobuffersizebytes.md)
  The size of the buffer that the extended audio file object’s associated audio converter uses to read or write the associated audio file. Value is a read/write `UInt32`.
- [var kExtAudioFileProperty_IOBuffer: ExtAudioFilePropertyID](kextaudiofileproperty_iobuffer.md)
  An audio data buffer. Value is a read/write `void*` value.
- [var kExtAudioFileProperty_PacketTable: ExtAudioFilePropertyID](kextaudiofileproperty_packettable.md)
  This property can be used to override the priming and remainder information in an audio file, and also to retrieve the current priming and remainder frames information for an extended audio file object. If the underlying file type does not provide packet table information, attempting to get the value of this property returns an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientmaxpacketsize)*