# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Reads a video file as an async sequence of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to url: URL, eventHandler: EventHandler?) async throws -> VideoReader.AsyncFrames
```

#### Return Value

An async sequence of `VideoFrames`.

## Parameters

- `url`: A video file URL.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/applied(to:eventhandler:))*