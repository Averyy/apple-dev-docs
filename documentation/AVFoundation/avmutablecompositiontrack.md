# AVMutableCompositionTrack

**Framework**: AVFoundation  
**Kind**: class

A mutable track in a composition that you use to insert, remove, and scale track segments without affecting their low-level representation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMutableCompositionTrack
```

#### Overview

Use this object to define constraints for the temporal arrangement of the track segments. If you set the composition’s track segments, you can test whether they meet the constraints by calling the [`validateSegments(_:)`](avmutablecompositiontrack/validatesegments(_:).md) method.

## Topics

### Configuring Track Properties
- [var isEnabled: Bool](avmutablecompositiontrack/isenabled.md)
  A Boolean value that indicates whether the tracks is in an enabled state.
- [var naturalTimeScale: CMTimeScale](avmutablecompositiontrack/naturaltimescale.md)
  The time scale in which you can perform time-based operations without extra numerical conversion.
- [var languageCode: String?](avmutablecompositiontrack/languagecode.md)
  The language associated with the track, as an ISO 639-2/T language code.
- [var extendedLanguageTag: String?](avmutablecompositiontrack/extendedlanguagetag.md)
  The language tag associated with the track, as an RFC 4646 language tag.
- [var preferredTransform: CGAffineTransform](avmutablecompositiontrack/preferredtransform.md)
  The preferred transformation of the visual media data for display purposes.
- [var preferredVolume: Float](avmutablecompositiontrack/preferredvolume.md)
  The volume the track prefers for its audible media data.
### Managing Time Ranges
- [var segments: [AVCompositionTrackSegment]!](avmutablecompositiontrack/segments.md)
  The track segments that a composition track contains.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablecompositiontrack/insertemptytimerange(_:).md)
  Adds or extends an empty time range within the track.
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime) throws](avmutablecompositiontrack/inserttimerange(_:of:at:).md)
  Inserts a time range of media from a source track into a composition track.
- [func insertTimeRanges([NSValue], of: [AVAssetTrack], at: CMTime) throws](avmutablecompositiontrack/inserttimeranges(_:of:at:).md)
  Inserts the time ranges of multiple source tracks into a track of a composition.
- [func removeTimeRange(CMTimeRange)](avmutablecompositiontrack/removetimerange(_:).md)
  Removes a time range of media from a composition track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecompositiontrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range of the track.
### Associating Tracks
- [func addTrackAssociation(to: AVCompositionTrack, type: AVAssetTrack.AssociationType)](avmutablecompositiontrack/addtrackassociation(to:type:).md)
  Establishes a track association of a specific type between two tracks.
- [func removeTrackAssociation(to: AVCompositionTrack, type: AVAssetTrack.AssociationType)](avmutablecompositiontrack/removetrackassociation(to:type:).md)
  Removes an association from a composition track.
### Replacing Format Descriptions
- [func replaceFormatDescription(CMFormatDescription, with: CMFormatDescription?)](avmutablecompositiontrack/replaceformatdescription(_:with:).md)
  Replaces a format description with another or cancels a previous replacement.
### Validating Segments
- [func validateSegments([AVCompositionTrackSegment]) throws](avmutablecompositiontrack/validatesegments(_:).md)
  Returns a Boolean value that indicates whether a given array of track segments conform to the timing rules for a composition track.

## Relationships

### Inherits From
- [AVCompositionTrack](avcompositiontrack.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMutableComposition](avmutablecomposition.md)
  An object that you use to create a new composition from existing assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack)*