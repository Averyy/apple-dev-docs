# ExtAudioFileTell(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets an audio file’s read/write position.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileTell(_ inExtAudioFile: ExtAudioFileRef, _ outFrameOffset: UnsafeMutablePointer<Int64>) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object that represents the file you are working with.
- `outFrameOffset`: On output, the file’s current read/write position in sample frames. Read/write position is specified in the sample rate and frame count of the file’s audio data format—not your application’s audio data format.

## See Also

- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](extaudiofileread(_:_:_:).md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](extaudiofileseek(_:_:).md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](extaudiofilewrite(_:_:_:).md)
  Performs a synchronous, sequential write operation on an audio file.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](extaudiofilewriteasync(_:_:_:).md)
  Perform an asynchronous, sequential write operation on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofiletell(_:_:))*