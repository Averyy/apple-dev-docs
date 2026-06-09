# init(delegate:)

**Framework**: ScreenCaptureKit  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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