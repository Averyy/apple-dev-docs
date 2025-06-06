# CNScript

**Framework**: Cinematic  
**Kind**: class

A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final class CNScript
```

#### Overview

The Cinematic script provides thread-safe access to information about the focus decisions made in the original recorded Cinematic movie. The script supports changing those decisions and obtaining updated information about where to focus each frame. You can snapshot changes to a script and later reload them.

> 💡 **Tip**:  Look up what you need up front, outside your critical code, and pass the immutable results to where it’s needed. That way, you’re not blocked when you access the information inside the rendering portion of your code.

 Look up what you need up front, outside your critical code, and pass the immutable results to where it’s needed. That way, you’re not blocked when you access the information inside the rendering portion of your code.

## Topics

### Structures
- [CNScript.Changes](cnscript-1ispe/changes.md)
  An object that represents a snapshot of the changes made to a movie script, including the added user decisions and detection tracks.
- [CNScript.Frame](cnscript-1ispe/frame.md)
  An object that represents what to focus on, and where to focus, in a given movie frame.
### Initializers
- [init(asset: AVAsset, changes: CNScript.Changes?, progress: Progress?) async throws](cnscript-1ispe/init(asset:changes:progress:).md)
  Creates a Cinematic script based on a movie and applying changes to the movie.
### Instance Properties
- [var addedDetectionTracks: [CNDetectionTrack]](cnscript-1ispe/addeddetectiontracks.md)
  An array of the detection tracks added since recording the original Cinematic movie.
- [var fNumber: Float](cnscript-1ispe/fnumber.md)
  The f-stop value which inversely affects the aperture used to render the Cinematic image.
- [var timeRange: CMTimeRange](cnscript-1ispe/timerange.md)
  The time range of the selected track.
### Instance Methods
- [func addDetectionTrack(CNDetectionTrack) -> CNDetectionID](cnscript-1ispe/adddetectiontrack(_:).md)
  Adds a user-created detection track.
- [func addUserDecision(CNDecision) -> Bool](cnscript-1ispe/adduserdecision(_:).md)
  Adds a new user decision, and replaces an existing user decision if the times are identical.
- [func baseDecisions(in: CMTimeRange) -> [CNDecision]](cnscript-1ispe/basedecisions(in:).md)
  All base decisions made automatically during recording in the given time range.
- [func changes() -> CNScript.Changes](cnscript-1ispe/changes.md)
  Changes made since recording the Cinematic asset.
- [func changes(trimmedBy: CMTimeRange) -> CNScript.Changes](cnscript-1ispe/changes(trimmedby:).md)
  Changes trimmed and time range shifted to start at zero.
- [func decision(after: CMTime) -> CNDecision?](cnscript-1ispe/decision(after:).md)
  The decision that occurs after the given time.
- [func decision(at: CMTime, tolerance: CMTime) -> CNDecision?](cnscript-1ispe/decision(at:tolerance:).md)
  The closest decision to the given time within the given tolerance.
- [func decision(before: CMTime) -> CNDecision?](cnscript-1ispe/decision(before:).md)
  The decision that occurs before the given time.
- [func decisions(in: CMTimeRange) -> [CNDecision]](cnscript-1ispe/decisions(in:).md)
  All decisions within the given time range.
- [func detectionTrack(for: CNDecision) -> CNDetectionTrack?](cnscript-1ispe/detectiontrack(for:)-1xvsa.md)
  A detection track representing all detections selected by a given decision.
- [func detectionTrack(for: CNDetectionID) -> CNDetectionTrack?](cnscript-1ispe/detectiontrack(for:)-6f8mk.md)
  A detection track representing all detections with the given detection ID, over the entire Cinematic script.
- [func frame(at: CMTime, tolerance: CMTime) -> CNScript.Frame?](cnscript-1ispe/frame(at:tolerance:).md)
  The closest frame to the given time within the given tolerance.
- [func frames(in: CMTimeRange) -> [CNScript.Frame]](cnscript-1ispe/frames(in:).md)
  All frames within the given time range.
- [func primaryDecision(at: CMTime) -> CNDecision?](cnscript-1ispe/primarydecision(at:).md)
  The primary decision that’s in effect at the specified time, unless it’s outside the time range of the Cinematic script.
- [func reload(changes: CNScript.Changes?)](cnscript-1ispe/reload(changes:).md)
  Reloads the Cinematic script with optional changes applied, removing any previous changes made.
- [func removeAllUserDecisions()](cnscript-1ispe/removealluserdecisions.md)
  Removes all user decisions and reverts to base decisions only.
- [func removeDetectionTrack(CNDetectionTrack) -> Bool](cnscript-1ispe/removedetectiontrack(_:).md)
  Removes the user-created detection track.
- [func removeUserDecision(CNDecision) -> Bool](cnscript-1ispe/removeuserdecision(_:).md)
  Removes an existing user decision.
- [func secondaryDecision(at: CMTime) -> CNDecision?](cnscript-1ispe/secondarydecision(at:).md)
  If a given time is during a focus transition, the system transitions toward a secondary decision.
- [func timeRangeOfTransition(after: CNDecision) -> CMTimeRange](cnscript-1ispe/timerangeoftransition(after:).md)
  The time range during which the focus transitioned away from the given decision.
- [func timeRangeOfTransition(before: CNDecision) -> CMTimeRange](cnscript-1ispe/timerangeoftransition(before:).md)
  The time range during which the focus transitioned toward the given decision.
- [func userDecisions(in: CMTimeRange) -> [CNDecision]](cnscript-1ispe/userdecisions(in:).md)
  All user decisions in the given time range.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Playing and editing Cinematic mode video](playing-and-editing-cinematic-mode-video.md)
  Play and edit Cinematic mode video with an adjustable depth of field and focus points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe)*