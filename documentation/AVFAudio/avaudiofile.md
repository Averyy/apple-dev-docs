# AVAudioFile

**Framework**: AVFAudio  
**Kind**: class

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

#### Overview

Regardless of the file format, you read and write using [`AVAudioPCMBuffer`](avaudiopcmbuffer.md) objects. These objects contain samples as [`AVAudioCommonFormat`](avaudiocommonformat.md) that the framework refers to as the file’s processing format. You convert to and from using the file’s actual format.

Reads and writes are always sequential. Random access is possible by setting the [`framePosition`](avaudiofile/frameposition.md) property.

## Topics

### Creating an Audio File
- [init(forReading: URL) throws](avaudiofile/init(forreading:).md)
  Opens a file for reading using the standard, deinterleaved floating point format.
- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](avaudiofile/init(forreading:commonformat:interleaved:).md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](avaudiofile/init(forwriting:settings:).md)
  Opens a file for writing using the specified settings.
- [init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](avaudiofile/init(forwriting:settings:commonformat:interleaved:).md)
  Opens a file for writing using a specified processing format and settings.
### Reading and Writing the Audio Buffer
- [func read(into: AVAudioPCMBuffer) throws](avaudiofile/read(into:).md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](avaudiofile/read(into:framecount:).md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func write(from: AVAudioPCMBuffer) throws](avaudiofile/write(from:).md)
  Writes an audio buffer sequentially.
- [func close()](avaudiofile/close.md)
  Closes the audio file.
### Getting Audio File Properties
- [var url: URL](avaudiofile/url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](avaudiofile/fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](avaudiofile/processingformat.md)
  The processing format of the file.
- [var length: AVAudioFramePosition](avaudiofile/length.md)
  The number of sample frames in the file.
- [typealias AVAudioFramePosition](avaudioframeposition.md)
  A position in an audio file or stream.
- [var framePosition: AVAudioFramePosition](avaudiofile/frameposition.md)
  The position in the file where the next read or write operation occurs.
- [typealias AVAudioFrameCount](avaudioframecount.md)
  A number of audio sample frames.
- [let AVAudioFileTypeKey: String](avaudiofiletypekey.md)
  A string that indicates the audio file type.
- [var isOpen: Bool](avaudiofile/isopen.md)
  A Boolean value that indicates whether the file is open.
### Initializers
- [init()](avaudiofile/init.md)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAudioBuffer](avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioTime](avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile)*