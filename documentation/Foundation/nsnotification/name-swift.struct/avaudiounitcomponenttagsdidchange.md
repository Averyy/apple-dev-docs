# AVAudioUnitComponentTagsDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

### AVFAudio
- [static let AVAudioEngineConfigurationChange: NSNotification.Name](./avaudioengineconfigurationchange.md)
  A notification the framework posts when the audio engine configuration changes.
- [class let interruptionNotification: NSNotification.Name](../../../AVFAudio/avaudiosession/interruptionnotification.md)
  A notification the system posts when an audio interruption occurs.
- [class let mediaServicesWereLostNotification: NSNotification.Name](../../../AVFAudio/avaudiosession/mediaserviceswerelostnotification.md)
  A notification the system posts when it terminates the media server.
- [class let mediaServicesWereResetNotification: NSNotification.Name](../../../AVFAudio/avaudiosession/mediaserviceswereresetnotification.md)
  A notification the system posts when the media server restarts.
- [class let routeChangeNotification: NSNotification.Name](../../../AVFAudio/avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](../../../AVFAudio/avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange)*