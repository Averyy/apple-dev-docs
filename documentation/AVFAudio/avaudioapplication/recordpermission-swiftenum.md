# AVAudioApplication.recordPermission

**Framework**: AVFAudio  
**Kind**: enum

Constants that indicate the app’s permission to record audio.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum recordPermission
```

## Topics

### Permissions
- [AVAudioApplication.recordPermission.undetermined](avaudioapplication/recordpermission-swift.enum/undetermined.md)
  Indicates the app hasn’t requested recording permission.
- [AVAudioApplication.recordPermission.granted](avaudioapplication/recordpermission-swift.enum/granted.md)
  Indicates the user grants the app permission to record audio.
- [AVAudioApplication.recordPermission.denied](avaudioapplication/recordpermission-swift.enum/denied.md)
  Indicates the user denies the app permission to record audio.
### Initializers
- [init?(rawValue: Int)](avaudioapplication/recordpermission-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func requestRecordPermission(completionHandler: (Bool) -> Void)](avaudioapplication/requestrecordpermission(completionhandler:).md)
  Determines whether the app has permission to record audio.
- [var recordPermission: AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.property.md)
  The app’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/recordpermission-swift.enum)*