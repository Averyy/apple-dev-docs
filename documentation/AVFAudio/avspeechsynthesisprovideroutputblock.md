# AVSpeechSynthesisProviderOutputBlock

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(NSArray<AVSpeechSynthesisMarker *> *, AVSpeechSynthesisProviderRequest *) AVSpeechSynthesisProviderOutputBlock;
```

## Parameters

- `markers`: An array of speech synthesis metadata.
- `speechRequest`: A speech request the system associates with the metadata.

## See Also

### Supplying metadata
- [var speechSynthesisOutputMetadataBlock: AVSpeechSynthesisProviderOutputBlock?](./avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md)
  A block that subclasses use to send marker information to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideroutputblock)*