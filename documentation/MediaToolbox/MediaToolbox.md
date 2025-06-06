# Media Toolbox

**Framework**: Media Toolbox  
**Kind**: module

Enable support for media format readers; tap and process audio from an audio mix.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

Call the [`MTRegisterProfessionalVideoWorkflowFormatReaders()`](mtregisterprofessionalvideoworkflowformatreaders().md) function to enable the use of custom [`MediaExtension`](https://developer.apple.com/documentation/MediaExtension) format readers.

Use an [`MTAudioProcessingTap`](mtaudioprocessingtap.md) to tap audio from an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer).

## Topics

### Professional video workflows
- [func MTRegisterProfessionalVideoWorkflowFormatReaders()](mtregisterprofessionalvideoworkflowformatreaders().md)
  Enables the use of media format readers that support professional video workflows.
### Audio Taps
- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus](mtaudioprocessingtapcreate(_:_:_:_:).md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](mtaudioprocessingtapgetstorage(_:).md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](mtaudioprocessingtapgettypeid().md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](mtaudioprocessingtap.md)
  An audio processing tap object.
### Utility
- [func MTCopyLocalizedNameForMediaType(CMMediaType) -> CFString?](mtcopylocalizednameformediatype(_:).md)
  Returns a localized name for the specified media type.
- [func MTCopyLocalizedNameForMediaSubType(CMMediaType, FourCharCode) -> CFString?](mtcopylocalizednameformediasubtype(_:_:).md)
  Returns a localized name for the specified media type and subtype.
### Enumerations
- [Anonymous Enumerations](anonymous-enums.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaToolbox)*