# setPreferredMicrophoneInjectionMode(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred mode of injecting audio into another app’s input stream.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
func setPreferredMicrophoneInjectionMode(_ inValue: AVAudioSession.MicrophoneInjectionMode) throws
```

```objc
- (BOOL) setPreferredMicrophoneInjectionMode:(AVAudioSessionMicrophoneInjectionMode) inValue error:(NSError **) outError;
```

## Parameters

- `inValue`: The preferred microphone injection mode.

## See Also

### Enabling adding audio to calls
- [var isMicrophoneInjectionAvailable: Bool](./ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](./preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](./microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](./microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredmicrophoneinjectionmode(_:))*