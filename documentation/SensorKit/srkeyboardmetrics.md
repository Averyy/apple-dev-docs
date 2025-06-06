# SRKeyboardMetrics

**Framework**: SensorKit  
**Kind**: class

The configuration of a device’s keyboard and its usage patterns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRKeyboardMetrics
```

#### Overview

The [`keyboardMetrics`](srsensor/keyboardmetrics.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Inspecting Keyboard Configuration and Sessions
- [var duration: TimeInterval](srkeyboardmetrics/duration.md)
  The duration that the report spans.
- [var keyboardIdentifier: String](srkeyboardmetrics/keyboardidentifier.md)
  The identifier of the keyboard in the keyboard list.
- [var version: String](srkeyboardmetrics/version.md)
  The version of keyboard metrics.
- [var width: Measurement<UnitLength>](srkeyboardmetrics/width.md)
  The width, in millimeters, of the keyboard in the report.
- [var height: Measurement<UnitLength>](srkeyboardmetrics/height.md)
  The height, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](srkeyboardmetrics/inputmodes.md)
  The active keyboard languages in the session.
- [var sessionIdentifiers: [String]](srkeyboardmetrics/sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.
### Quantifying Key Use
- [var totalWords: Int](srkeyboardmetrics/totalwords.md)
  The total number of typed words for the keyboard.
- [var totalAlteredWords: Int](srkeyboardmetrics/totalalteredwords.md)
  The total number of altered words for the keyboard.
- [var totalTaps: Int](srkeyboardmetrics/totaltaps.md)
  The total number of taps for the keyboard.
- [var totalDrags: Int](srkeyboardmetrics/totaldrags.md)
  The total number of drags for the keyboard.
- [var totalDeletes: Int](srkeyboardmetrics/totaldeletes.md)
  The total number of deletions for the keyboard.
- [var totalEmojis: Int](srkeyboardmetrics/totalemojis.md)
  The total number of emojis for the keyboard.
- [var totalPaths: Int](srkeyboardmetrics/totalpaths.md)
  The total number of completed paths for the keyboard.
- [var totalPathTime: TimeInterval](srkeyboardmetrics/totalpathtime.md)
  The total time to complete paths for the keyboard.
- [var totalPathLength: Measurement<UnitLength>](srkeyboardmetrics/totalpathlength.md)
  The total length of completed paths for the keyboard.
- [var totalAutoCorrections: Int](srkeyboardmetrics/totalautocorrections.md)
  The total number of autocorrections for the keyboard.
- [var totalSpaceCorrections: Int](srkeyboardmetrics/totalspacecorrections.md)
  The total number of space corrections for the keyboard.
- [var totalRetroCorrections: Int](srkeyboardmetrics/totalretrocorrections.md)
  The total number of retro corrections for the keyboard.
- [var totalTranspositionCorrections: Int](srkeyboardmetrics/totaltranspositioncorrections.md)
  The total number of transposition corrections for the keyboard.
- [var totalInsertKeyCorrections: Int](srkeyboardmetrics/totalinsertkeycorrections.md)
  The total number of Insert key corrections for the keyboard.
- [var totalSkipTouchCorrections: Int](srkeyboardmetrics/totalskiptouchcorrections.md)
  The total number of skip touch corrections for the keyboard.
- [var totalNearKeyCorrections: Int](srkeyboardmetrics/totalnearkeycorrections.md)
  The total number of near key corrections for the keyboard.
- [var totalSubstitutionCorrections: Int](srkeyboardmetrics/totalsubstitutioncorrections.md)
  The total number of substitution corrections for the keyboard.
- [var totalHitTestCorrections: Int](srkeyboardmetrics/totalhittestcorrections.md)
  The total number of hit test corrections for the keyboard.
- [var totalTypingDuration: TimeInterval](srkeyboardmetrics/totaltypingduration.md)
  The total amount of typing time for the keyboard.
- [var totalPathPauses: Int](srkeyboardmetrics/totalpathpauses.md)
  The total number of pauses while drawing a path for a word.
- [var totalPauses: Int](srkeyboardmetrics/totalpauses.md)
  The total number of pauses during the session.
- [var totalTypingEpisodes: Int](srkeyboardmetrics/totaltypingepisodes.md)
  The total number of continuous typing episodes during the session.
### Timing Key Use
- [SRKeyboardMetrics.ProbabilityMetric](srkeyboardmetrics/probabilitymetric.md)
  A likelihood of occurrence.
- [var touchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdownup.md)
  The duration between touch down to touch up for any key.
- [var touchUpDown: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchupdown.md)
  The duration between touch up and touch down for any key.
- [var spaceTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetouchdownup.md)
  The duration between touch down and touch up of all Space bar events for the keyboard.
- [var deleteTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetouchdownup.md)
  The duration between touch down and touch up of all Delete key events for the keyboard.
- [var shortWordCharKeyTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytouchdownup.md)
  The duration between touch down and touch up of all character keys in short words for the keyboard.
- [var touchDownDown: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdowndown.md)
  The duration between touch down and touch down for any key.
- [var charKeyToPrediction: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoprediction.md)
  The duration between touch up on a character key and touch down on a word in the prediction bar.
- [var shortWordCharKeyToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytocharkey.md)
  The duration between touch up on a character key and touch down on any sequential character key in a short word.
- [var charKeyToAnyTapKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoanytapkey.md)
  The duration between touch up on a character key and touch down on the next sequential key.
- [var anyTapToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/anytaptocharkey.md)
  The duration between touch up of any key and touch down on a sequential character key.
- [var spaceToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetocharkey.md)
  The duration between touch up of the Space bar and touch down of a sequential character key.
- [var charKeyToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytospacekey.md)
  The duration between touch up of a character key and touch down of a sequential Space bar.
- [var spaceToDeleteKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetodeletekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Delete key.
- [var deleteToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetospacekey.md)
  The duration between touch up of the Delete key and touch down of a sequential Space bar.
- [var spaceToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetospacekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Space bar.
- [var spaceToShiftKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetoshiftkey.md)
  The duration between touch up of the Space bar and touch down of a sequential Shift key.
- [var spaceToPlaneChangeKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetoplanechangekey.md)
  The duration between touch up of the Space bar and touch down of a sequential plane change key.
- [var spaceToPredictionKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetopredictionkey.md)
  The duration between touch up of the Space bar and touch down of a sequential selection from the prediction bar.
- [var deleteToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetocharkey.md)
  The duration between touch up of the Delete key and touch down of a sequential character key.
- [var charKeyToDelete: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytodelete.md)
  The duration between touch up of a character key and touch down of a sequential Delete key.
- [var deleteToDelete: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetodelete.md)
  The duration between touch up of the Delete key and touch down of a sequential Delete key.
- [var deleteToDeletes: [ProbabilityMetric<UnitDuration>]](srkeyboardmetrics/deletetodeletes.md)
  The duration between touch up of the Delete key and touch down of a sequential Delete key for an entire word.
- [var deleteToShiftKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetoshiftkey.md)
  The duration between touch up of the Delete key and touch down of a sequential Shift key.
- [var deleteToPlaneChangeKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetoplanechangekey.md)
  The duration between touch up of the Delete key and touch down of a sequential plane change key.
- [var anyTapToPlaneChangeKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/anytaptoplanechangekey.md)
  The duration between touch up of any key and touch down on a plane change key.
- [var planeChangeToAnyTap: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/planechangetoanytap.md)
  The duration between touch up on a plane change key and touch down on the next sequential key.
- [var charKeyToPlaneChangeKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoplanechangekey.md)
  The duration between touch up of a character key and touch down of a sequential plane change key.
- [var planeChangeKeyToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/planechangekeytocharkey.md)
  The duration between touch up of a plane change key and touch down of any key.
- [var deleteToPath: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetopath.md)
  The duration between touch up of the Delete key and touch down of a sequential path.
- [var pathToDelete: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/pathtodelete.md)
  The duration between touch up of the Delete key and touch down of a continuous path.
- [var spaceToPath: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetopath.md)
  The duration between touch up of the Space bar and touch down to begin a sequential path.
- [var pathToSpace: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/pathtospace.md)
  The duration between touch up of a path and touch down of a sequential Space bar.
- [var pathToPath: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/pathtopath.md)
  The duration between touch up of a path and touch down of a sequential path.
- [var longWordTouchDownUp: [ProbabilityMetric<UnitDuration>]](srkeyboardmetrics/longwordtouchdownup.md)
  The duration between touch down and touch up of the character keys of all the long words in the session.
- [var longWordTouchDownDown: [ProbabilityMetric<UnitDuration>]](srkeyboardmetrics/longwordtouchdowndown.md)
  The duration between touch down and touch down of the character keys of all the long words in the session.
- [var longWordTouchUpDown: [ProbabilityMetric<UnitDuration>]](srkeyboardmetrics/longwordtouchupdown.md)
  The duration between touch up and touch down of the character keys of all the long words in the session.
- [var pathTypingSpeed: Double](srkeyboardmetrics/pathtypingspeed.md)
  The QuickType words per minute in the session.
- [var typingSpeed: Double](srkeyboardmetrics/typingspeed.md)
  The user’s typing rate in characters per second.
### Measuring Key Use
- [var longWordUpErrorDistance: [ProbabilityMetric<UnitLength>]](srkeyboardmetrics/longworduperrordistance.md)
  The distance from the touch up to the center of the intended key of the characters of a long word.
- [var longWordDownErrorDistance: [ProbabilityMetric<UnitLength>]](srkeyboardmetrics/longworddownerrordistance.md)
  The distance from the touch down to the center of the intended key of the characters of a long word.
- [var upErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/uperrordistance.md)
  The distance from the touch up to the center of any key.
- [var downErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/downerrordistance.md)
  The distance from the touch down to the center of any key.
- [var spaceUpErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/spaceuperrordistance.md)
  The distance from the touch up to the right centroid of the Space bar.
- [var spaceDownErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/spacedownerrordistance.md)
  The distance from the touch down to the right centroid of the Space bar.
- [var deleteUpErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/deleteuperrordistance.md)
  The distance from the touch up to the center of the Delete key.
- [var deleteDownErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/deletedownerrordistance.md)
  The distance from the touch down to the center of the Delete key.
- [var shortWordCharKeyUpErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/shortwordcharkeyuperrordistance.md)
  The distance from the touch up to the center of the intended key of a character in a short word.
- [var shortWordCharKeyDownErrorDistance: ProbabilityMetric<UnitLength>](srkeyboardmetrics/shortwordcharkeydownerrordistance.md)
  The distance from the touch down to the center of the intended key of a character in a short word.
- [var pathErrorDistanceRatio: [NSNumber]](srkeyboardmetrics/patherrordistanceratio.md)
  Sample values of the ratio of error distance between the intended and actual path.
### Inferring Sentiment
- [func wordCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](srkeyboardmetrics/wordcount(for:).md)
  Provides the number of typed words for the specified sentiment in the report.
- [func emojiCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](srkeyboardmetrics/emojicount(for:).md)
  Provides the number of typed emojis for the specified sentiment in the report.
- [SRKeyboardMetrics.SentimentCategory](srkeyboardmetrics/sentimentcategory.md)
  Moods that the framework determines by analyzing the user’s input.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SRAmbientLightSample](srambientlightsample.md)
  The amount of ambient light in the user’s environment.
- [class SRDeviceUsageReport](srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRMediaEvent](srmediaevent.md)
  A user interaction with a media object, such as an image or a video.
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)*