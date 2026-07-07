# speedMultiplier

**Framework**: Core Media  
**Kind**: property

The factor by which the sample buffer’s presentation should be accelerated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let speedMultiplier: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Float>
```

#### Discussion

For normal playback the speed multiplier would be 1.0 (which is the default value returned by getter if this attachment is not present); for double-speed playback the speed multiplier would be 2.0, which would halve the output duration. Speed-multiplication factors take effect after trimming; see [`outputDuration`](cmreadysamplebuffer/outputduration.md). Note that this attachment principally provides information about the duration-stretching effect: by default, it should be implemented by rate conversion, but other attachments may specify richer stretching operations—for example, scaling without pitch shift, or pitch shift without changing duration. Sequences of speed-multiplied sample buffers should have explicit time stamps to clarify when each should be output (see [`outputPresentationTimeStamp`](cmreadysamplebuffer/outputpresentationtimestamp.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/speedmultiplier)*