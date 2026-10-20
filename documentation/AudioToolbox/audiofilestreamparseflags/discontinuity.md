# discontinuity

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Type Property

Pass this flag to the [`AudioFileStreamParseBytes(_:_:_:_:)`](../audiofilestreamparsebytes%28_,_,_,_%29.md) function to signal a discontinuity in the audio data.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var discontinuity: AudioFileStreamParseFlags { get }
```

```c
kAudioFileStreamParseFlag_Discontinuity
```

#### Discussion

Any partial packet straddling a buffer boundary is discarded to avoid having the parser call your callback with a corrupt packet. After a discontinuity occurs, the [`AudioFileStreamSeek(_:_:_:_:)`](../audiofilestreamseek%28_,_,_,_%29.md) function might return approximate values for some data formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags/discontinuity)*