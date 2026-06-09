# init(filter:configuration:delegate:)

**Framework**: ScreenCaptureKit  
**Kind**: init

Creates a stream with a content filter and configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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