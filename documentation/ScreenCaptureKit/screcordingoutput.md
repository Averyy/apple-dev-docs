# SCRecordingOutput

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 15.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class SCRecordingOutput
```

```objc
@interface SCRecordingOutput : NSObject
```

## Topics

### Creating a recording output
- [init(configuration: SCRecordingOutputConfiguration, delegate: any SCRecordingOutputDelegate)](./screcordingoutput/init%28configuration,delegate%29.md)
- [class SCRecordingOutputConfiguration](./screcordingoutputconfiguration.md)
- [protocol SCRecordingOutputDelegate](./screcordingoutputdelegate.md)
### Monitoring recording progress
- [var recordedDuration: CMTime](./screcordingoutput/recordedduration.md)
- [var recordedFileSize: Int](./screcordingoutput/recordedfilesize.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Adding and removing recording output
- [func addRecordingOutput(SCRecordingOutput) throws](./scstream/addrecordingoutput%28_%29.md)
- [func removeRecordingOutput(SCRecordingOutput) throws](./scstream/removerecordingoutput%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingoutput)*