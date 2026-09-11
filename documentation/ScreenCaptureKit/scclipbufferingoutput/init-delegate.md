# init(delegate:)

**Framework**: ScreenCaptureKit  
**Kind**: init

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(delegate: (any SCClipBufferingOutputDelegate)?)
```

#### Discussion

Initialize SCClipBufferingOutput object with SCClipBufferingOutputDelegate

Client can create a SCClipBufferingOutput with this initializer and add it to SCStream to start clip buffering.

## Parameters

- `delegate`: Object conforming to SCClipBufferingOutputDelegate protocol. Clients may specify a delegate to receive notifications about clip buffering events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutput/init(delegate:))*