# dontPageAlignAudioData

**Framework**: Audio Toolbox  
**Kind**: property

Typically, the audio data in a file is page aligned. To make reading the file data as fast as possible, you can use page-aligned data to take advantage of optimized code paths in the file system. However, when space is at a premium, you might want to avoid the additional padding required to attain alignment. To do so, set this flag when calling [`AudioFileCreate`](audiofilecreate.md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var dontPageAlignAudioData: AudioFileFlags { get }
```

## See Also

- [static var eraseFile: AudioFileFlags](audiofileflags/erasefile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/dontpagealignaudiodata)*