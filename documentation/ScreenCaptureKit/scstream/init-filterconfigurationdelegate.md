# init(filter:configuration:delegate:)

**Framework**: ScreenCaptureKit  
**Kind**: init

Creates a stream with a content filter and configuration.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
init(filter contentFilter: SCContentFilter, configuration streamConfig: SCStreamConfiguration, delegate: (any SCStreamDelegate)?)
```

## Parameters

- `contentFilter`: The content to capture.
- `streamConfig`: The configuration to apply to the stream.
- `delegate`: An optional object that responds to stream events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/init(filter:configuration:delegate:))*