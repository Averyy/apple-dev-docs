# recordPermission

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The current recording permission status.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 10.0

> **Deprecated**: Use [`recordPermission`](../avaudioapplication/recordpermission-swift.property.md) on [`AVAudioApplication`](../avaudioapplication.md) instead.

## Declaration

```swift
var recordPermission: AVAudioSession.RecordPermission { get }
```

```objc
@property (readonly) AVAudioSessionRecordPermission recordPermission;
```

## Return Value

Returns one of three status values:

## Discussion

- The user granted permission to record ([`AVAudioSession.RecordPermission.granted`](./recordpermission-swift.enum/granted.md)).
- The user denied recording permission ([`AVAudioSession.RecordPermission.denied`](./recordpermission-swift.enum/denied.md)).
- Recording permission hasn’t been requested ([`AVAudioSession.RecordPermission.undetermined`](./recordpermission-swift.enum/undetermined.md)).

## Topics

### Permission states
- [AVAudioSession.RecordPermission](./recordpermission-swift.enum.md)
  The values that define the current state of the record permission request.

## See Also

### Requesting permission to record
- [func requestRecordPermission((Bool) -> Void)](./requestrecordpermission%28_%29.md)
  Requests the user’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/recordpermission-swift.property)*