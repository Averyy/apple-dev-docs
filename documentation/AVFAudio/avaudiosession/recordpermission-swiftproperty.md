# recordPermission

**Framework**: AVFAudio  
**Kind**: property

The current recording permission status.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var recordPermission: AVAudioSession.RecordPermission { get }
```

#### Return Value

Returns one of three status values:

#### Discussion

- The user granted permission to record ([`AVAudioSession.RecordPermission.granted`](avaudiosession/recordpermission-swift.enum/granted.md)).
- The user denied recording permission ([`AVAudioSession.RecordPermission.denied`](avaudiosession/recordpermission-swift.enum/denied.md)).
- Recording permission hasn’t been requested ([`AVAudioSession.RecordPermission.undetermined`](avaudiosession/recordpermission-swift.enum/undetermined.md)).

## Topics

### Data Types
- [AVAudioSession.RecordPermission](avaudiosession/recordpermission-swift.enum.md)
  The values that define the current state of the record permission request.

## See Also

- [func requestRecordPermission((Bool) -> Void)](avaudiosession/requestrecordpermission(_:).md)
  Requests the user’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/recordpermission-swift.property)*