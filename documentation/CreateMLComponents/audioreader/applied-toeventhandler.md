# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Reads an audio file as an async sequence of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to url: URL, eventHandler: EventHandler? = nil) throws -> AudioReader.AsyncBuffers
```

#### Return Value

An async sequence of `AVAudioPCMBuffer`.

## Parameters

- `url`: An audio file URL.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/applied(to:eventhandler:))*