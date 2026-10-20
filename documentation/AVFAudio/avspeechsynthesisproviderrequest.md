# AVSpeechSynthesisProviderRequest

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVSpeechSynthesisProviderRequest : NSObject
```

## Topics

### Creating a request
- [init(ssmlRepresentation: String, voice: AVSpeechSynthesisProviderVoice)](./avspeechsynthesisproviderrequest/init%28ssmlrepresentation,voice%29-7elh.md)
  Creates a request with a voice and a description.
### Inspecting a request
- [var ssmlRepresentation: String](./avspeechsynthesisproviderrequest/ssmlrepresentation.md)
  The description of the text to synthesize.
- [var voice: AVSpeechSynthesisProviderVoice](./avspeechsynthesisproviderrequest/voice.md)
  The voice to use in the speech request.
- [class AVSpeechSynthesisProviderVoice](./avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.
### Initializers
- [init(SSMLRepresentation: String, voice: AVSpeechSynthesisProviderVoice)](./avspeechsynthesisproviderrequest/init%28ssmlrepresentation,voice%29-5v77t.md)
- [init?(coder: NSCoder)](./avspeechsynthesisproviderrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Rendering speech
- [func synthesizeSpeechRequest(AVSpeechSynthesisProviderRequest)](./avspeechsynthesisprovideraudiounit/synthesizespeechrequest%28_%29.md)
  Sets the text to synthesize and the voice to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisproviderrequest)*