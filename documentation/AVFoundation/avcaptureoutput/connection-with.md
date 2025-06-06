# connection(with:)

**Framework**: AVFoundation  
**Kind**: method

Returns the first connection with an input port of a specified media type.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func connection(with mediaType: AVMediaType) -> AVCaptureConnection?
```

#### Return Value

The first capture connection that has the specified media type, or `nil` if no connection for the media type exists.

## Parameters

- `mediaType`: A media type such as   or  .

## See Also

- [var connections: [AVCaptureConnection]](avcaptureoutput/connections.md)
  The capture output object’s connections.
- [AVCaptureOutput.DataDroppedReason](avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/connection(with:))*