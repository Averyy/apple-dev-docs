# eraseFile

**Framework**: Audio Toolbox  
**Kind**: property

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var eraseFile: AudioFileFlags { get }
```

#### Discussion

If set, the [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md) function erases the contents of an existing file. If not set, then the function fails if the file already exists.

## See Also

- [static var dontPageAlignAudioData: AudioFileFlags](audiofileflags/dontpagealignaudiodata.md)
  Typically, the audio data in a file is page aligned. To make reading the file data as fast as possible, you can use page-aligned data to take advantage of optimized code paths in the file system. However, when space is at a premium, you might want to avoid the additional padding required to attain alignment. To do so, set this flag when calling [`AudioFileCreate`](audiofilecreate.md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/erasefile)*