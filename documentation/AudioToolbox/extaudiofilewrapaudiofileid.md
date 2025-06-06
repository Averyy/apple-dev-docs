# ExtAudioFileWrapAudioFileID(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Wraps an audio file object in an extended audio file object.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Bool, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Allocates a new extended audio file object that wraps an existing audio file object. Your application is responsible for keeping the audio file object open until the extended audio file object is disposed.

## Parameters

- `inFileID`: The audio file object to wrap.
- `inForWriting`: Use   if you intend to write to the audio file,   otherwise.
- `outExtAudioFile`: On output, a newly allocated extended audio file object.

## See Also

- [func ExtAudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>?, UInt32, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofilecreatewithurl(_:_:_:_:_:_:).md)
  Creates a new audio file and associates it with a new extended audio file object.
- [func ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus](extaudiofiledispose(_:).md)
  Disposes of an extended audio file object and closes the associated file.
- [func ExtAudioFileOpenURL(CFURL, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofileopenurl(_:_:).md)
  Opens an existing audio file for reading, and associates it with a new extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilewrapaudiofileid(_:_:_:))*