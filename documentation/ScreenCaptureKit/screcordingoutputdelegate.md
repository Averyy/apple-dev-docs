# SCRecordingOutputDelegate

**Framework**: ScreenCaptureKit  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 15.0+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol SCRecordingOutputDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func recordingOutput(SCRecordingOutput, didFailWithError: any Error)](screcordingoutputdelegate/recordingoutput(_:didfailwitherror:).md)
- [func recordingOutputDidFinishRecording(SCRecordingOutput)](screcordingoutputdelegate/recordingoutputdidfinishrecording(_:).md)
- [func recordingOutputDidStartRecording(SCRecordingOutput)](screcordingoutputdelegate/recordingoutputdidstartrecording(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [init(configuration: SCRecordingOutputConfiguration, delegate: any SCRecordingOutputDelegate)](screcordingoutput/init(configuration:delegate:).md)
- [class SCRecordingOutputConfiguration](screcordingoutputconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingoutputdelegate)*