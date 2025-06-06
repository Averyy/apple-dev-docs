# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs conversion of the input audio buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to input: AVAudioPCMBuffer, eventHandler: EventHandler? = nil) throws -> AVAudioPCMBuffer
```

#### Return Value

An output audio buffer by converting the input buffer to the `targetFormat`.

## Parameters

- `input`: The audio buffer that will be converted.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioconvertingtransformer/applied(to:eventhandler:))*