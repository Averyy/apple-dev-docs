# addStreamOutput(_:type:sampleHandlerQueue:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Adds a destination that receives the stream output.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func addStreamOutput(_ output: any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws
```

```objc
- (BOOL) addStreamOutput:(id<SCStreamOutput>) output type:(SCStreamOutputType) type sampleHandlerQueue:(dispatch_queue_t) sampleHandlerQueue error:(NSError **) error;
```

#### Discussion

Use this method to attach an object that conforms to [`SCStreamOutput`](../scstreamoutput.md) to receive stream content. Optionally, provide a [`DispatchQueue`](../../Dispatch/dispatchqueue.md) to send output to a queue that’s responsible for processing the output.

## Parameters

- `output`: The object that conforms to the stream output protocol.
- `type`: The stream output type.
- `sampleHandlerQueue`: The queue that receives the stream output.

## See Also

### Adding and removing stream output
- [func removeStreamOutput(any SCStreamOutput, type: SCStreamOutputType) throws](./removestreamoutput%28_,type%29.md)
  Removes a destination from receiving stream output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/addstreamoutput(_:type:samplehandlerqueue:))*