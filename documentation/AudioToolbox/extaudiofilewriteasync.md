# ExtAudioFileWriteAsync(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Perform an asynchronous, sequential write operation on an audio file.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileWriteAsync(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Writes the provided buffer list to an internal ring buffer and notifies an internal thread to perform the write at a later time. The first time this function is called, allocations may be performed. You can call this function with `0` frames and a `NULL` buffer in a non-time-critical context to initialize the asynchronous mechanism. Once initialized, subsequent calls are very efficient and do not take locks. This technique may be used to write to a file from a realtime thread.

Your application must not mix synchronous and asynchronous writes to the same file.

Pending writes are not guaranteed to be flushed to disk until the [`ExtAudioFileDispose(_:)`](extaudiofiledispose(_:).md) function is called.

Errors may occur after this call has returned. Such errors may be returned from subsequent calls to this function.

## Parameters

- `inExtAudioFile`: The extended audio file object that represents the file you want to write to.
- `inNumberFrames`: The number of frames to write.
- `ioData`: The buffer(s) from which audio data is written to the file.

## See Also

- [func ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](extaudiofileread(_:_:_:).md)
  Performs a synchronous, sequential read operation on an audio file.
- [func ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus](extaudiofileseek(_:_:).md)
  Seeks to a specified frame in a file.
- [func ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus](extaudiofiletell(_:_:).md)
  Gets an audio file’s read/write position.
- [func ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus](extaudiofilewrite(_:_:_:).md)
  Performs a synchronous, sequential write operation on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilewriteasync(_:_:_:))*