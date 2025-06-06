# recordPermission

**Framework**: AVFAudio  
**Kind**: property

The app’s permission to record audio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var recordPermission: AVAudioApplication.recordPermission { get }
```

#### Discussion

See [`requestRecordPermission(completionHandler:)`](avaudioapplication/requestrecordpermission(completionhandler:).md) for more information.

## See Also

- [class func requestRecordPermission(completionHandler: (Bool) -> Void)](avaudioapplication/requestrecordpermission(completionhandler:).md)
  Determines whether the app has permission to record audio.
- [AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.enum.md)
  Constants that indicate the app’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/recordpermission-swift.property)*