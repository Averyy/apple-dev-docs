# ExtAudioFileWrite(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Performs a synchronous, sequential write operation on an audio file.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileWrite(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

If the extended audio file object has an application data format, then the object’s converter converts the data in the `ioData` parameter to the file data format.

## Parameters

- `inExtAudioFile`: The extended audio file object that represents the file to write to.
- `inNumberFrames`: The number of frames to write.
- `ioData`: The buffer(s) from which audio data is written to the file.

## See Also

- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](extaudiofileread(_:_:_:).md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](extaudiofileseek(_:_:).md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](extaudiofiletell(_:_:).md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](extaudiofilewriteasync(_:_:_:).md)
  Perform an asynchronous, sequential write operation on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilewrite(_:_:_:))*