# AVAudioUnitComponentTagsDidChange

**Framework**: Foundation  
**Kind**: property

A notification that indicates when component tags change.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let AVAudioUnitComponentTagsDidChange: NSNotification.Name
```

#### Discussion

The notification object contains the `AVAudioUnitComponent` object with the tags.

## See Also

- [static let AVAudioEngineConfigurationChange: NSNotification.Name](nsnotification/name-swift.struct/avaudioengineconfigurationchange.md)
  A notification the framework posts when the audio engine configuration changes.
- [class let interruptionNotification: NSNotification.Name](../AVFAudio/AVAudioSession/interruptionNotification.md)
  A notification the system posts when an audio interruption occurs.
- [class let mediaServicesWereLostNotification: NSNotification.Name](../AVFAudio/AVAudioSession/mediaServicesWereLostNotification.md)
  A notification the system posts when it terminates the media server.
- [class let mediaServicesWereResetNotification: NSNotification.Name](../AVFAudio/AVAudioSession/mediaServicesWereResetNotification.md)
  A notification the system posts when the media server restarts.
- [class let routeChangeNotification: NSNotification.Name](../AVFAudio/AVAudioSession/routeChangeNotification.md)
  A notification the system posts when its audio route changes.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](../AVFAudio/AVAudioSession/silenceSecondaryAudioHintNotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange)*