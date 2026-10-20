# recordPermission

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAudioApplicationRecordPermission recordPermission;
```

#### Discussion

See [`requestRecordPermission(completionHandler:)`](./requestrecordpermission%28completionhandler%29.md) for more information.

## See Also

### Requesting audio recording permission
- [class func requestRecordPermission(completionHandler: (Bool) -> Void)](./requestrecordpermission%28completionhandler%29.md)
  Determines whether the app has permission to record audio.
- [AVAudioApplication.recordPermission](./recordpermission-swift.enum.md)
  Constants that indicate the app’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/recordpermission-swift.property)*