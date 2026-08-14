# AVSpeechSynthesisProviderRequest

**Framework**: AVFAudio  
**Kind**: class

An object that represents the text to synthesize and the voice to use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class AVSpeechSynthesisProviderRequest
```

## Topics

### Creating a request
- [init(ssmlRepresentation: String, voice: AVSpeechSynthesisProviderVoice)](avspeechsynthesisproviderrequest/init(ssmlrepresentation:voice:)-7elh.md)
  Creates a request with a voice and a description.
### Inspecting a request
- [var ssmlRepresentation: String](avspeechsynthesisproviderrequest/ssmlrepresentation.md)
  The description of the text to synthesize.
- [var voice: AVSpeechSynthesisProviderVoice](avspeechsynthesisproviderrequest/voice.md)
  The voice to use in the speech request.
- [class AVSpeechSynthesisProviderVoice](avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.
### Initializers
- [init(SSMLRepresentation: String, voice: AVSpeechSynthesisProviderVoice)](avspeechsynthesisproviderrequest/init(ssmlrepresentation:voice:)-5v77t.md)
- [init?(coder: NSCoder)](avspeechsynthesisproviderrequest/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func synthesizeSpeechRequest(AVSpeechSynthesisProviderRequest)](avspeechsynthesisprovideraudiounit/synthesizespeechrequest(_:).md)
  Sets the text to synthesize and the voice to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisproviderrequest)*