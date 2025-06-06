# SHSignatureGenerator

**Framework**: ShazamKit  
**Kind**: class

An object for converting audio data into a signature.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class SHSignatureGenerator
```

## Mentions

- [Generating a signature from an audio buffer](generating-a-signature-from-an-audio-buffer.md)

#### Overview

Create both reference and query signatures using this class.

## Topics

### Generating a signature from audio
- [func append(AVAudioPCMBuffer, at: AVAudioTime?) throws](shsignaturegenerator/append(_:at:).md)
  Adds audio to the generator.
- [func signature() -> SHSignature](shsignaturegenerator/signature.md)
  Converts the audio buffer into a signature.
- [Generating a signature from an audio buffer](generating-a-signature-from-an-audio-buffer.md)
  Create a signature from an audio file or the microphone for a reference track in a custom catalog, or for matching tracks in a catalog.
### Generate a signature from assets
- [class func generateSignature(from: AVAsset, completionHandler: (SHSignature?, (any Error)?) -> Void)](shsignaturegenerator/generatesignature(from:completionhandler:).md)
  Creates a signature with the asset you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SHSignature](shsignature.md)
  An object that contains the opaque data and other information for a signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignaturegenerator)*