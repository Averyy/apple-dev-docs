# SCStream

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

An instance that represents a stream of shareable content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class SCStream
```

```objc
@interface SCStream : NSObject
```

## Overview

Use a stream to capture video of screen content like apps and windows. Create a content stream by passing it an instance of [`SCContentFilter`](./sccontentfilter.md) and an [`SCStreamConfiguration`](./scstreamconfiguration.md) object. The stream uses the filter to determine which screen content to capture, and uses the configuration data to configure the output.

## Topics

### Creating a stream
- [init(filter: SCContentFilter, configuration: SCStreamConfiguration, delegate: (any SCStreamDelegate)?)](./scstream/init%28filter,configuration,delegate%29.md)
  Creates a stream with a content filter and configuration.
### Updating stream configuration
- [func updateConfiguration(SCStreamConfiguration, completionHandler: (((any Error)?) -> Void)?)](./scstream/updateconfiguration%28_,completionhandler%29.md)
  Updates the stream with a new configuration.
- [func updateContentFilter(SCContentFilter, completionHandler: (((any Error)?) -> Void)?)](./scstream/updatecontentfilter%28_,completionhandler%29.md)
  Updates the stream by applying a new content filter.
### Adding and removing stream output
- [func addStreamOutput(any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws](./scstream/addstreamoutput%28_,type,samplehandlerqueue%29.md)
  Adds a destination that receives the stream output.
- [func removeStreamOutput(any SCStreamOutput, type: SCStreamOutputType) throws](./scstream/removestreamoutput%28_,type%29.md)
  Removes a destination from receiving stream output.
### Adding and removing recording output
- [func addRecordingOutput(SCRecordingOutput) throws](./scstream/addrecordingoutput%28_%29.md)
- [func removeRecordingOutput(SCRecordingOutput) throws](./scstream/removerecordingoutput%28_%29.md)
- [class SCRecordingOutput](./screcordingoutput.md)
### Starting and stopping a stream
- [func startCapture(completionHandler: (((any Error)?) -> Void)?)](./scstream/startcapture%28completionhandler%29.md)
  Starts the stream with a callback to indicate whether it successfully starts.
- [func stopCapture(completionHandler: (((any Error)?) -> Void)?)](./scstream/stopcapture%28completionhandler%29.md)
  Stops the stream.
### Stream synchronization
- [var synchronizationClock: CMClock?](./scstream/synchronizationclock.md)
  A clock to use for output synchronization.
### Instance Properties
- [var isCapturing: Bool](./scstream/iscapturing.md)
### Instance Methods
- [func addClipBufferingOutput(SCClipBufferingOutput) throws](./scstream/addclipbufferingoutput%28_%29.md)
- [func addVideoEffectOutput(SCVideoEffectOutput) throws](./scstream/addvideoeffectoutput%28_%29.md)
- [func removeClipBufferingOutput(SCClipBufferingOutput) throws](./scstream/removeclipbufferingoutput%28_%29.md)
- [func removeVideoEffectOutput(SCVideoEffectOutput) throws](./scstream/removevideoeffectoutput%28_%29.md)

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

### Content capture
- [class SCStreamConfiguration](./scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](./sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](./scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](./scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](./scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](./scscreenshotoutput.md)
  An object that contains all images requested by the client.
- [class SCVideoEffectOutput](./scvideoeffectoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream)*