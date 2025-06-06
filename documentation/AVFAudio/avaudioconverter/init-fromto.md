# init(from:to:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio converter object from the specified input and output formats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(from fromFormat: AVAudioFormat, to toFormat: AVAudioFormat)
```

#### Return Value

An [`AVAudioConverter`](avaudioconverter.md) instance, or `nil` if the format conversion isn’t possible.

## Parameters

- `fromFormat`: The input audio format.
- `toFormat`: The audio format to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/init(from:to:))*