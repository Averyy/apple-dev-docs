# SCStream

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that represents a stream of shareable content.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCStream
```

#### Overview

Use a stream to capture video of screen content like apps and windows. Create a content stream by passing it an instance of [`SCContentFilter`](sccontentfilter.md) and an [`SCStreamConfiguration`](scstreamconfiguration.md) object. The stream uses the filter to determine which screen content to capture, and uses the configuration data to configure the output.

## Topics

### Creating a stream
- [init(filter: SCContentFilter, configuration: SCStreamConfiguration, delegate: (any SCStreamDelegate)?)](scstream/init(filter:configuration:delegate:).md)
  Creates a stream with a content filter and configuration.
### Updating stream configuration
- [func updateConfiguration(SCStreamConfiguration, completionHandler: (((any Error)?) -> Void)?)](scstream/updateconfiguration(_:completionhandler:).md)
  Updates the stream with a new configuration.
- [func updateContentFilter(SCContentFilter, completionHandler: (((any Error)?) -> Void)?)](scstream/updatecontentfilter(_:completionhandler:).md)
  Updates the stream by applying a new content filter.
### Adding and removing stream output
- [func addStreamOutput(any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws](scstream/addstreamoutput(_:type:samplehandlerqueue:).md)
  Adds a destination that receives the stream output.
- [func removeStreamOutput(any SCStreamOutput, type: SCStreamOutputType) throws](scstream/removestreamoutput(_:type:).md)
  Removes a destination from receiving stream output.
### Adding and removing recording output
- [func addRecordingOutput(SCRecordingOutput) throws](scstream/addrecordingoutput(_:).md)
- [func removeRecordingOutput(SCRecordingOutput) throws](scstream/removerecordingoutput(_:).md)
- [class SCRecordingOutput](screcordingoutput.md)
### Starting and stopping a stream
- [func startCapture(completionHandler: (((any Error)?) -> Void)?)](scstream/startcapture(completionhandler:).md)
  Starts the stream with a callback to indicate whether it successfully starts.
- [func stopCapture(completionHandler: (((any Error)?) -> Void)?)](scstream/stopcapture(completionhandler:).md)
  Stops the stream.
### Stream synchronization
- [var synchronizationClock: CMClock?](scstream/synchronizationclock.md)
  A clock to use for output synchronization.

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

- [class SCStreamConfiguration](scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream)*