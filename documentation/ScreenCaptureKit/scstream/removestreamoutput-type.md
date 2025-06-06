# removeStreamOutput(_:type:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Removes a destination from receiving stream output.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func removeStreamOutput(_ output: any SCStreamOutput, type: SCStreamOutputType) throws
```

## Parameters

- `output`: The object to remove that conforms to the stream output protocol.
- `type`: The stream output type.

## See Also

- [func addStreamOutput(any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws](scstream/addstreamoutput(_:type:samplehandlerqueue:).md)
  Adds a destination that receives the stream output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/removestreamoutput(_:type:))*