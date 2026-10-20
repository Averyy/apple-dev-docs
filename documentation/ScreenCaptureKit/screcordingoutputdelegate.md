# SCRecordingOutputDelegate

**Framework**: ScreenCaptureKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 15.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol SCRecordingOutputDelegate : NSObjectProtocol
```

```objc
@protocol SCRecordingOutputDelegate <NSObject>
```

## Topics

### Instance Methods
- [func recordingOutput(SCRecordingOutput, didFailWithError: any Error)](./screcordingoutputdelegate/recordingoutput%28_,didfailwitherror%29.md)
- [func recordingOutputDidFinishRecording(SCRecordingOutput)](./screcordingoutputdelegate/recordingoutputdidfinishrecording%28_%29.md)
- [func recordingOutputDidStartRecording(SCRecordingOutput)](./screcordingoutputdelegate/recordingoutputdidstartrecording%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a recording output
- [init(configuration: SCRecordingOutputConfiguration, delegate: any SCRecordingOutputDelegate)](./screcordingoutput/init%28configuration,delegate%29.md)
- [class SCRecordingOutputConfiguration](./screcordingoutputconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingoutputdelegate)*