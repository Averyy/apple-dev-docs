# ExtAudioFileSeek(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Seeks to a specified frame in a file.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileSeek(_ inExtAudioFile: ExtAudioFileRef, _ inFrameOffset: Int64) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Sets the file’s read position to the specified sample frame number. A subsequent call to the [`ExtAudioFileRead(_:_:_:)`](extaudiofileread(_:_:_:).md) function returns samples from precisely this location, even if it is located in the middle of a packet.

Ensure that the file you are seeking in is open for reading only. This function’s behavior with files open for writing is undefined.

## Parameters

- `inExtAudioFile`: The extended audio file object that represents the file you are working with.
- `inFrameOffset`: The desired seek position, in sample frames, relative to the beginning of the file. Seek position is specified in the sample rate and frame count of the file’s audio data format—not your application’s audio data format.

## See Also

- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](extaudiofileread(_:_:_:).md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](extaudiofiletell(_:_:).md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](extaudiofilewrite(_:_:_:).md)
  Performs a synchronous, sequential write operation on an audio file.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](extaudiofilewriteasync(_:_:_:).md)
  Perform an asynchronous, sequential write operation on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofileseek(_:_:))*