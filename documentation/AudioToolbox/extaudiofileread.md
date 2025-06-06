# ExtAudioFileRead(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Performs a synchronous, sequential read operation on an audio file.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileRead(_ inExtAudioFile: ExtAudioFileRef, _ ioNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

If the extended audio file object has an application data format, then the object’s converter converts the file data to the application format.

This function works only on a single thread. If you want your application to read an audio file on multiple threads, use Audio File Services instead.

## Parameters

- `inExtAudioFile`: The extended audio file object that represents the file you want to read.
- `ioNumberFrames`: On input, the number of frames to read from the file. On output, the number of frames actually read. Fewer frames may be read than were requested. For example, the supplied buffers may not be large enough to accommodate the requested data. If   frames are returned, end-of-file was reached.
- `ioData`: One or more buffers into which the audio data is read.

## See Also

- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](extaudiofileseek(_:_:).md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](extaudiofiletell(_:_:).md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](extaudiofilewrite(_:_:_:).md)
  Performs a synchronous, sequential write operation on an audio file.
- [func ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>?) -> OSStatus](extaudiofilewriteasync(_:_:_:).md)
  Perform an asynchronous, sequential write operation on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofileread(_:_:_:))*