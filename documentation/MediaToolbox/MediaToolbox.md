# Media Toolbox

**Framework**: Media Toolbox  
**Kind**: module  
**Role**: Framework

Enable support for media format readers; tap and process audio from an audio mix.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Overview

Call the [`MTRegisterProfessionalVideoWorkflowFormatReaders()`](./mtregisterprofessionalvideoworkflowformatreaders%28%29.md) function to enable the use of custom [MediaExtension](../MediaExtension/MediaExtension.md) format readers.

Use an [`MTAudioProcessingTap`](./mtaudioprocessingtap.md) to tap audio from an [`AVPlayer`](../AVFoundation/avplayer.md).

## Topics

### Professional video workflows
- [func MTRegisterProfessionalVideoWorkflowFormatReaders()](./mtregisterprofessionalvideoworkflowformatreaders%28%29.md)
  Enables the use of media format readers that support professional video workflows.
### Audio Taps
- [func MTAudioProcessingTapCreate(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus](./mtaudioprocessingtapcreate%28_,_,_,_%29.md)
  Creates a new audio processing tap.
- [func MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>?, UnsafeMutablePointer<CMTimeRange>?, UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./mtaudioprocessingtapgetsourceaudio%28_,_,_,_,_,_%29.md)
  Retrieves source audio for an audio processing tap.
- [func MTAudioProcessingTapGetStorage(MTAudioProcessingTap) -> UnsafeMutableRawPointer](./mtaudioprocessingtapgetstorage%28_%29.md)
  Retrieves a custom storage pointer for an audio processing tap.
- [func MTAudioProcessingTapGetTypeID() -> CFTypeID](./mtaudioprocessingtapgettypeid%28%29.md)
  Retrieves the type identifier for this audio processing tap.
- [typealias MTAudioProcessingTapFlags](./mtaudioprocessingtapflags.md)
  Flags that indicate where to tap the audio.
- [class MTAudioProcessingTap](./mtaudioprocessingtap.md)
  An audio processing tap object.
### Utility
- [func MTCopyLocalizedNameForMediaType(CMMediaType) -> CFString?](./mtcopylocalizednameformediatype%28_%29.md)
  Returns a localized name for the specified media type.
- [func MTCopyLocalizedNameForMediaSubType(CMMediaType, FourCharCode) -> CFString?](./mtcopylocalizednameformediasubtype%28_,_%29.md)
  Returns a localized name for the specified media type and subtype.
### Enumerations
- [Anonymous Enumerations](./anonymous-enums.md)
### Functions
- [func MTAudioProcessingTapCreateWithPreferredFormat(CFAllocator?, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, CMAudioFormatDescription?, UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus](./mtaudioprocessingtapcreatewithpreferredformat%28_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaToolbox)*