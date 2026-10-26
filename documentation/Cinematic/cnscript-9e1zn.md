# CNScript

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNScript : NSObject
```

#### Overview

The Cinematic script provides thread-safe access to information about the focus decisions made in the original recorded Cinematic movie. The script supports changing those decisions and obtaining updated information about where to focus each frame. You can snapshot changes to a script and later reload them.

> 💡 **Tip**:  Look up what you need up front, outside your critical code, and pass the immutable results to where it’s needed. That way, you’re not blocked when you access the information inside the rendering portion of your code.

## Topics

### Instance Properties
- [addedDetectionTracks](./cnscript-9e1zn/addeddetectiontracks.md)
  An array of the detection tracks added since recording the original Cinematic movie.
- [fNumber](./cnscript-9e1zn/fnumber.md)
  The f-stop value that inversely affects the aperture used to render the Cinematic image.
- [timeRange](./cnscript-9e1zn/timerange.md)
  The time range of the Cinematic asset.
### Instance Methods
- [- addDetectionTrack:](./cnscript-9e1zn/adddetectiontrack_.md)
  Adds a user-created detection track.
- [- addUserDecision:](./cnscript-9e1zn/adduserdecision_.md)
  Adds a new user decision, and replaces an existing user decision if the times are identical.
- [- baseDecisionsInTimeRange:](./cnscript-9e1zn/basedecisionsintimerange_.md)
  All base decisions made automatically during recording in the given time range.
- [- changes](./cnscript-9e1zn/changes.md)
  Changes made since recording the Cinematic asset.
- [- changesTrimmedByTimeRange:](./cnscript-9e1zn/changestrimmedbytimerange_.md)
  Changes trimmed and time range shifted to start at zero.
- [- decisionAfterTime:](./cnscript-9e1zn/decisionaftertime_.md)
  The decision that occurs after the given time.
- [- decisionAtTime:tolerance:](./cnscript-9e1zn/decisionattime_tolerance_.md)
  The closest frame to the given time within the given tolerance.
- [- decisionBeforeTime:](./cnscript-9e1zn/decisionbeforetime_.md)
  The decision that occurs before the given time.
- [- decisionsInTimeRange:](./cnscript-9e1zn/decisionsintimerange_.md)
  All decisions within the given time range.
- [- detectionTrackForDecision:](./cnscript-9e1zn/detectiontrackfordecision_.md)
  A detection track representing all detections selected by a given decision.
- [- detectionTrackForID:](./cnscript-9e1zn/detectiontrackforid_.md)
  A detection track representing all detections with the given detection ID, over the entire Cinematic script.
- [- frameAtTime:tolerance:](./cnscript-9e1zn/frameattime_tolerance_.md)
  The closest frame to the given time within the given tolerance.
- [- framesInTimeRange:](./cnscript-9e1zn/framesintimerange_.md)
  All frames within the given time range.
- [- primaryDecisionAtTime:](./cnscript-9e1zn/primarydecisionattime_.md)
  The primary decision that’s in effect at the specified time, unless it’s outside the time range of the Cinematic script.
- [- reloadWithChanges:](./cnscript-9e1zn/reloadwithchanges_.md)
  Reloads the Cinematic script with optional changes applied, removing any previous changes made.
- [- removeAllUserDecisions](./cnscript-9e1zn/removealluserdecisions.md)
  Removes all user decisions and reverts to base decisions only.
- [- removeDetectionTrack:](./cnscript-9e1zn/removedetectiontrack_.md)
  Removes the user-created detection track.
- [- removeUserDecision:](./cnscript-9e1zn/removeuserdecision_.md)
  Removes an existing user decision.
- [- secondaryDecisionAtTime:](./cnscript-9e1zn/secondarydecisionattime_.md)
  If a given time is during a focus transition, the system transitions toward a secondary decision.
- [- timeRangeOfTransitionAfterDecision:](./cnscript-9e1zn/timerangeoftransitionafterdecision_.md)
  The time range during which the focus transitioned away from the given decision.
- [- timeRangeOfTransitionBeforeDecision:](./cnscript-9e1zn/timerangeoftransitionbeforedecision_.md)
  The time range during which the focus transitioned toward the given decision.
- [- userDecisionsInTimeRange:](./cnscript-9e1zn/userdecisionsintimerange_.md)
  All user decisions in the given time range.
### Type Methods
- [+ loadFromAsset:changes:progress:completionHandler:](./cnscript-9e1zn/loadfromasset_changes_progress_completionhandler_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Essentials
- [Playing and editing Cinematic mode video](./playing-and-editing-cinematic-mode-video.md)
  Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- [CNScriptChanges](./cnscriptchanges.md)
  An object that represents a snapshot of the changes made to a movie script, including the added user decisions and detection tracks.
- [CNScriptFrame](./cnscriptframe.md)
  An object that represents what to focus on, and where to focus, in a given movie frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn)*