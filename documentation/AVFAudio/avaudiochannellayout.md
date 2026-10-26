# AVAudioChannelLayout

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that describes the roles of a set of audio channels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioChannelLayout
```

```objc
@interface AVAudioChannelLayout : NSObject
```

#### Overview

The `AVAudioChannelLayout` class is a thin wrapper for Core Audio’s [`AudioChannelLayout`](../CoreAudioTypes/audiochannellayout.md).

## Topics

### Creating an audio channel layout
- [init(layout: UnsafePointer<AudioChannelLayout>)](./avaudiochannellayout/init%28layout%29.md)
  Creates an audio channel layout object from an existing one.
- [convenience init?(layoutTag: AudioChannelLayoutTag)](./avaudiochannellayout/init%28layouttag%29.md)
  Creates an audio channel layout object from a layout tag.
- [+ layoutWithLayout:](./avaudiochannellayout/layoutwithlayout_.md)
  Creates an audio channel layout object from an existing one.
- [+ layoutWithLayoutTag:](./avaudiochannellayout/layoutwithlayouttag_.md)
  Creates an audio channel layout object from an audio channel layout tag.
### Getting audio channel layout properties
- [typealias AVAudioChannelCount](./avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](./avaudiochannellayout/channelcount.md)
  The number of channels of audio data.
- [var layout: UnsafePointer<AudioChannelLayout>](./avaudiochannellayout/layout.md)
  The underlying audio channel layout.
- [var layoutTag: AudioChannelLayoutTag](./avaudiochannellayout/layouttag.md)
  The audio channel’s underlying layout tag.
- [func isEqual(Any) -> Bool](./avaudiochannellayout/isequal%28_%29.md)
  Indicates whether another audio channel layout is exactly equal to the current layout.
### Initializers
- [init?(coder: NSCoder)](./avaudiochannellayout/init%28coder%29.md)

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
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio data
- [class AVAudioFile](./avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioPCMBuffer](./avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.
- [class AVAudioCompressedBuffer](./avaudiocompressedbuffer.md)
  An object that represents an audio buffer that you use for compressed audio formats.
- [struct AVReadOnlyAudioPCMBuffer](./avreadonlyaudiopcmbuffer.md)
  A read-only, Sendable audio buffer for safe concurrent access.
- [class AVAudioBuffer](./avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioFormat](./avaudioformat.md)
  An object that describes the representation of an audio format.
- [class AVAudioConverter](./avaudioconverter.md)
  An object that converts streams of audio between formats.
- [class AVAudioTime](./avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](./audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout)*