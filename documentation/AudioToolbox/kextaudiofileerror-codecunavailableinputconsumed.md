# kExtAudioFileError_CodecUnavailableInputConsumed

**Framework**: Audio Toolbox  
**Kind**: var

The [`ExtAudioFileWrite(_:_:_:)`](extaudiofilewrite(_:_:_:).md) function was interrupted and the last buffer that you provided was successfully written to disk.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kExtAudioFileError_CodecUnavailableInputConsumed: OSStatus { get }
```

#### Discussion

For additional information, refer to [`Audio Guidelines By App Type`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioGuidelinesByAppType/AudioGuidelinesByAppType.html#//apple_ref/doc/uid/TP40007875-CH11) in [`Audio Session Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_codecunavailableinputconsumed)*