# removeStreamOutput(_:type:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Removes a destination from receiving stream output.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func removeStreamOutput(_ output: any SCStreamOutput, type: SCStreamOutputType) throws
```

```objc
- (BOOL) removeStreamOutput:(id<SCStreamOutput>) output type:(SCStreamOutputType) type error:(NSError **) error;
```

## Parameters

- `output`: The object to remove that conforms to the stream output protocol.
- `type`: The stream output type.

## See Also

### Adding and removing stream output
- [func addStreamOutput(any SCStreamOutput, type: SCStreamOutputType, sampleHandlerQueue: dispatch_queue_t?) throws](./addstreamoutput%28_,type,samplehandlerqueue%29.md)
  Adds a destination that receives the stream output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/removestreamoutput(_:type:))*