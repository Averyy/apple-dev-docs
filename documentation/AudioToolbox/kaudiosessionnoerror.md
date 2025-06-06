# kAudioSessionNoError

**Framework**: Audio Toolbox  
**Kind**: var

No error has occurred.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionNoError: Int { get }
```

## See Also

- [var kAudioSessionNotInitialized: Int](kaudiosessionnotinitialized.md)
  An Audio Session function was called without first initializing the session. To avoid this error, call the `AudioSessionInitialize` function before attempting to use the session.
- [var kAudioSessionAlreadyInitialized: Int](kaudiosessionalreadyinitialized.md)
  The `AudioSessionInitialize` function was called more than once during the lifetime of your application.
- [var kAudioSessionInitializationError: Int](kaudiosessioninitializationerror.md)
  There was an error during audio session initialization.
- [var kAudioSessionUnsupportedPropertyError: Int](kaudiosessionunsupportedpropertyerror.md)
  The audio session property is not supported.
- [var kAudioSessionBadPropertySizeError: Int](kaudiosessionbadpropertysizeerror.md)
  The size of the audio session property data was not correct.
- [var kAudioSessionNotActiveError: Int](kaudiosessionnotactiveerror.md)
  The audio operation failed because your application’s audio session was not active.
- [var kAudioServicesNoHardwareError: Int](kaudioservicesnohardwareerror.md)
  The audio operation failed because the device has no audio input available.
- [var kAudioSessionNoCategorySet: Int](kaudiosessionnocategoryset.md)
  The audio operation failed because it requires the audio session to have an explicitly-set category, but none was set. To use a hardware codec you must explicitly initialize the audio session and explicitly set an audio session category.
- [var kAudioSessionIncompatibleCategory: Int](kaudiosessionincompatiblecategory.md)
  The specified audio session category cannot be used for the attempted audio operation. For example, you attempted to play or record audio with the audio session category set to `kAudioSessionCategory_AudioProcessing`.
- [var kAudioSessionUnspecifiedError: Int](kaudiosessionunspecifiederror.md)
  An unspecified audio session error has occurred. This typically results from the audio system being in an inconsistent state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionnoerror)*