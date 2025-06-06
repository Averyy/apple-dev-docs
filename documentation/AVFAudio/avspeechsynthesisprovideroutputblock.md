# AVSpeechSynthesisProviderOutputBlock

**Framework**: AVFAudio  
**Kind**: typealias

A type that represents the method for sending marker information to the host.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias AVSpeechSynthesisProviderOutputBlock = ([AVSpeechSynthesisMarker], AVSpeechSynthesisProviderRequest) -> Void
```

## Parameters

- `markers`: An array of speech synthesis metadata.
- `speechRequest`: A speech request the system associates with the metadata.

## See Also

- [var speechSynthesisOutputMetadataBlock: AVSpeechSynthesisProviderOutputBlock?](avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md)
  A block that subclasses use to send marker information to the host.
- [class AVSpeechSynthesisMarker](avspeechsynthesismarker.md)
  An object that contains information about the synthesized audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideroutputblock)*