# ExtAudioFileOpenURL(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Opens an existing audio file for reading, and associates it with a new extended audio file object.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileOpenURL(_ inURL: CFURL, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus
```

```c
extern OSStatus ExtAudioFileOpenURL(CFURLRef inURL, ExtAudioFileRef*outExtAudioFile);
```

## Return Value

A result code.

## Parameters

- `inURL`: The audio file to read.
- `outExtAudioFile`: On output, a newly allocated extended audio file object.

## See Also

### Managing Extended Audio File Objects
- [func ExtAudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>?, UInt32, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md)
  Creates a new audio file and associates it with a new extended audio file object.
- [func ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus](./extaudiofiledispose%28_%29.md)
  Disposes of an extended audio file object and closes the associated file.
- [func ExtAudioFileWrapAudioFileID(AudioFileID, Bool, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilewrapaudiofileid%28_,_,_%29.md)
  Wraps an audio file object in an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofileopenurl(_:_:))*