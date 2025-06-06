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
- [init(ssmlRepresentation: String, voice: AVSpeechSynthesisProviderVoice)](avspeechsynthesisproviderrequest/init(ssmlrepresentation:voice:).md)
  Creates a request with a voice and a description.
### Inspecting a request
- [var ssmlRepresentation: String](avspeechsynthesisproviderrequest/ssmlrepresentation.md)
  The description of the text to synthesize.
- [var voice: AVSpeechSynthesisProviderVoice](avspeechsynthesisproviderrequest/voice.md)
  The voice to use in the speech request.
- [class AVSpeechSynthesisProviderVoice](avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func synthesizeSpeechRequest(AVSpeechSynthesisProviderRequest)](avspeechsynthesisprovideraudiounit/synthesizespeechrequest(_:).md)
  Sets the text to synthesize and the voice to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisproviderrequest)*