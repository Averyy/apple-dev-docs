# AVAudioFile

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents an audio file that the system can open for reading or writing.

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
class AVAudioFile
```

```objc
@interface AVAudioFile : NSObject
```

#### Overview

Regardless of the file format, you read and write using [`AVAudioPCMBuffer`](./avaudiopcmbuffer.md) objects. These objects contain samples as [`AVAudioCommonFormat`](./avaudiocommonformat.md) that the framework refers to as the file’s processing format. You convert to and from using the file’s actual format.

Reads and writes are always sequential. Random access is possible by setting the [`framePosition`](./avaudiofile/frameposition.md) property.

## Topics

### Creating an audio file
- [init(forReading: URL) throws](./avaudiofile/init%28forreading%29.md)
  Opens a file for reading using the standard, deinterleaved floating point format.
- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./avaudiofile/init%28forreading,commonformat,interleaved%29.md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](./avaudiofile/init%28forwriting,settings%29.md)
  Opens a file for writing using the specified settings.
- [init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./avaudiofile/init%28forwriting,settings,commonformat,interleaved%29.md)
  Opens a file for writing using a specified processing format and settings.
- [init()](./avaudiofile/init%28%29.md)
### Reading and writing audio
- [func read(into: AVAudioPCMBuffer) throws](./avaudiofile/read%28into%29.md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](./avaudiofile/read%28into,framecount%29.md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./avaudiofile/read%28framecount%29.md)
- [func write(from: AVAudioPCMBuffer) throws](./avaudiofile/write%28from%29-6qgec.md)
  Writes an audio buffer sequentially.
- [func write(from: AVReadOnlyAudioPCMBuffer) throws](./avaudiofile/write%28from%29-4zfhf.md)
- [func close()](./avaudiofile/close%28%29.md)
  Closes the audio file.
### Getting audio file properties
- [var url: URL](./avaudiofile/url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](./avaudiofile/fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](./avaudiofile/processingformat.md)
  The processing format of the file.
- [var length: AVAudioFramePosition](./avaudiofile/length.md)
  The number of sample frames in the file.
- [typealias AVAudioFramePosition](./avaudioframeposition.md)
  A position in an audio file or stream.
- [var framePosition: AVAudioFramePosition](./avaudiofile/frameposition.md)
  The position in the file where the next read or write operation occurs.
- [typealias AVAudioFrameCount](./avaudioframecount.md)
  A number of audio sample frames.
- [let AVAudioFileTypeKey: String](./avaudiofiletypekey.md)
  A string that indicates the audio file type.
- [var isOpen: Bool](./avaudiofile/isopen.md)
  A Boolean value that indicates whether the file is open.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio data
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
- [class AVAudioChannelLayout](./avaudiochannellayout.md)
  An object that describes the roles of a set of audio channels.
- [class AVAudioConverter](./avaudioconverter.md)
  An object that converts streams of audio between formats.
- [class AVAudioTime](./avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](./audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile)*