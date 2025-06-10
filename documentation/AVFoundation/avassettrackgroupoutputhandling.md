# AVAssetTrackGroupOutputHandling

**Framework**: AVFoundation  
**Kind**: struct

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

## Topics

### Policies
- [static var preserveAlternateTracks: AVAssetTrackGroupOutputHandling](avassettrackgroupoutputhandling/preservealternatetracks.md)
  A policy that passes through alternate audio tracks from the source asset during export.
### Initializers
- [init(rawValue: UInt)](avassettrackgroupoutputhandling/init(rawvalue:).md)
  Creates track group output handling structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var audioTrackGroupHandling: AVAssetTrackGroupOutputHandling](avassetexportsession/audiotrackgrouphandling.md)
  A policy that defines how the session exports alternate audio tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling)*