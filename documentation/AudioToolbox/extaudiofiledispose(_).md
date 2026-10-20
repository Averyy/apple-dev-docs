# ExtAudioFileDispose(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Disposes of an extended audio file object and closes the associated file.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileDispose(_ inExtAudioFile: ExtAudioFileRef) -> OSStatus
```

```c
extern OSStatus ExtAudioFileDispose(ExtAudioFileRef inExtAudioFile);
```

#### Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object to close.

## See Also

### Managing Extended Audio File Objects
- [func ExtAudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>?, UInt32, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md)
  Creates a new audio file and associates it with a new extended audio file object.
- [func ExtAudioFileOpenURL(CFURL, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofileopenurl%28_,_%29.md)
  Opens an existing audio file for reading, and associates it with a new extended audio file object.
- [func ExtAudioFileWrapAudioFileID(AudioFileID, Bool, UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](./extaudiofilewrapaudiofileid%28_,_,_%29.md)
  Wraps an audio file object in an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofiledispose(_:))*