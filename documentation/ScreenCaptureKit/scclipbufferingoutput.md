# SCClipBufferingOutput

**Framework**: ScreenCaptureKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class SCClipBufferingOutput
```

#### Overview

SCClipBufferingOutput

SCClipBufferingOutput represents a clip buffering session on a SCStream.

## Topics

### Initializers
- [init(delegate: (any SCClipBufferingOutputDelegate)?)](scclipbufferingoutput/init(delegate:).md)
### Instance Methods
- [func exportClip(to: URL, duration: TimeInterval, completionHandler: (((any Error)?) -> Void)?)](scclipbufferingoutput/exportclip(to:duration:completionhandler:).md)

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

- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [enum SCStreamOutputType](scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutput)*