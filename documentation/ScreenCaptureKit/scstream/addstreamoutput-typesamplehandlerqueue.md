# addStreamOutput(_:type:sampleHandlerQueue:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Adds a destination that receives the stream output.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func addStreamOutput(_ output: any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws
```

#### Discussion

Use this method to attach an object that conforms to [`SCStreamOutput`](scstreamoutput.md) to receive stream content. Optionally, provide a [`DispatchQueue`](https://developer.apple.com/documentation/Dispatch/DispatchQueue) to send output to a queue that’s responsible for processing the output.

## Parameters

- `output`: The object that conforms to the stream output protocol.
- `type`: The stream output type.
- `sampleHandlerQueue`: The queue that receives the stream output.

## See Also

- [func removeStreamOutput(any SCStreamOutput, type: SCStreamOutputType) throws](scstream/removestreamoutput(_:type:).md)
  Removes a destination from receiving stream output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/addstreamoutput(_:type:samplehandlerqueue:))*