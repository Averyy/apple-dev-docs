# AVAssetTrackGroupOutputHandling

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A type that specifies policies for how an export session processes alternate tracks in a track group.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AVAssetTrackGroupOutputHandling
```

```c
enum AVAssetTrackGroupOutputHandling : NSUInteger;
```

## Topics

### Policies
- [static var preserveAlternateTracks: AVAssetTrackGroupOutputHandling](./avassettrackgroupoutputhandling/preservealternatetracks.md)
  A policy that passes through alternate audio tracks from the source asset during export.
### Initializers
- [init(rawValue: UInt)](./avassettrackgroupoutputhandling/init%28rawvalue%29.md)
  Creates track group output handling structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Configuring track groups
- [var audioTrackGroupHandling: AVAssetTrackGroupOutputHandling](./avassetexportsession/audiotrackgrouphandling.md)
  A policy that defines how the session exports alternate audio tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling)*