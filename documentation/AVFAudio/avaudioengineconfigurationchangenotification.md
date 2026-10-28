# AVAudioEngineConfigurationChangeNotification

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A notification the framework posts when the audio engine configuration changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSString * const AVAudioEngineConfigurationChangeNotification;
```

## Discussion

When the audio engine’s I/O unit observes a change to the audio input or output hardware’s channel count or sample rate, the audio engine stops, uninitializes itself, and issues this notification. The nodes remain in an attached and connected state with the previously set formats. The app must reestablish connections if the connection formats need to change.

> **Note**:  Don’t deallocate the engine from within the client’s notification handler. The callback happens on an internal dispatch queue and can deadlock while trying to tear down the engine synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengineconfigurationchangenotification)*