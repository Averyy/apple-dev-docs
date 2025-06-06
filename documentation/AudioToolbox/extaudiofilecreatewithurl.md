# ExtAudioFileCreateWithURL(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new audio file and associates it with a new extended audio file object.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileCreateWithURL(_ inURL: CFURL, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>?, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

If the file to be created is in a compressed format, you may set the sample rate in the `inStreamDesc` parameter to `0`. In all cases, the extended file object’s encoding converter may produce audio at a different sample rate than the source. The file will be created with the audio format produced by the encoder.

## Parameters

- `inURL`: The URL of the new audio file.
- `inFileType`: The type of file to create, specified as a constant from the   enumeration.
- `inStreamDesc`: The format of the audio data to be written to the file.
- `inChannelLayout`: The channel layout of the audio data. If non-null, this must be consistent with the number of channels specified by the   parameter.
- `inFlags`: Flags for creating or opening the file. If the   flag is set, it erases an existing file. If the flag is not set, the function fails fails if the URL points to an existing file.
- `outExtAudioFile`: On output, a newly allocated extended audio file object.

## See Also

- [func ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus](extaudiofiledispose(_:).md)
  Disposes of an extended audio file object and closes the associated file.
- [func ExtAudioFileOpenURL(CFURL, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofileopenurl(_:_:).md)
  Opens an existing audio file for reading, and associates it with a new extended audio file object.
- [func ExtAudioFileWrapAudioFileID(AudioFileID, Bool, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](extaudiofilewrapaudiofileid(_:_:_:).md)
  Wraps an audio file object in an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilecreatewithurl(_:_:_:_:_:_:))*