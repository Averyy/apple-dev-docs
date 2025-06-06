# SCRecordingOutput

**Framework**: ScreenCaptureKit  
**Kind**: class

**Availability**:
- Mac Catalyst 18.2+
- macOS 15.0+

## Declaration

```swift
class SCRecordingOutput
```

## Topics

### Creating a recording output
- [init(configuration: SCRecordingOutputConfiguration, delegate: any SCRecordingOutputDelegate)](screcordingoutput/init(configuration:delegate:).md)
- [class SCRecordingOutputConfiguration](screcordingoutputconfiguration.md)
- [protocol SCRecordingOutputDelegate](screcordingoutputdelegate.md)
### Configuring the recording output
- [var recordedDuration: CMTime](screcordingoutput/recordedduration.md)
- [var recordedFileSize: Int](screcordingoutput/recordedfilesize.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addRecordingOutput(SCRecordingOutput) throws](scstream/addrecordingoutput(_:).md)
- [func removeRecordingOutput(SCRecordingOutput) throws](scstream/removerecordingoutput(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingoutput)*