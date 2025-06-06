# init(leadingFrames:trailingFrames:)

**Framework**: AVFAudio  
**Kind**: init

Creates a priming information instance with the specified leading and trailing frames.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(leadingFrames: AVAudioFrameCount, trailingFrames: AVAudioFrameCount)
```

## Parameters

- `leadingFrames`: Specifies the number of leading (previous) input frames relative to the start input frame.
- `trailingFrames`: Specifies the number of trailing input frames past the end input frame.

## See Also

- [init()](avaudioconverterprimeinfo/init.md)
  Creates a priming information instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimeinfo/init(leadingframes:trailingframes:))*