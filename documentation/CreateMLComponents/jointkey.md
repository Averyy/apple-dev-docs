# JointKey

**Framework**: Create ML Components  
**Kind**: struct

A key that uniquely identifies a joint.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct JointKey
```

## Topics

### Getting elbow properties
- [static let leftElbow: JointKey](jointkey/leftelbow.md)
  A key associated with left elbow joint in a body pose.
- [static let rightElbow: JointKey](jointkey/rightelbow.md)
  A key associated with right elbow joint in a body pose.
### Getting head properties
- [static let leftEye: JointKey](jointkey/lefteye.md)
  A key associated with left eye joint in a body pose.
- [static let rightEye: JointKey](jointkey/righteye.md)
  A key associated with right eye joint in a body pose.
- [static let leftEar: JointKey](jointkey/leftear.md)
  A key associated with left ear joint in a body pose.
- [static let rightEar: JointKey](jointkey/rightear.md)
  A key associated with right ear joint in a body pose.
- [static let nose: JointKey](jointkey/nose.md)
  A key associated with nose joint in a body pose.
### Getting index finger properties
- [static let indexDIP: JointKey](jointkey/indexdip.md)
  A key associated with index finger’s distal interphalangeal (DIP) joint in a hand pose.
- [static let indexMCP: JointKey](jointkey/indexmcp.md)
  A key associated with index finger’s metacarpophalangeal (MCP) joint in a hand pose.
- [static let indexPIP: JointKey](jointkey/indexpip.md)
  A key associated with index finger’s proximal interphalangeal (PIP) joint in a hand pose.
- [static let indexTip: JointKey](jointkey/indextip.md)
  A key associated with index finger tip joint in a hand pose.
### Getting little finger properties
- [static let littleDIP: JointKey](jointkey/littledip.md)
  A key associated with ring finger’s distal interphalangeal (DIP) joint in a hand pose.
- [static let littleMCP: JointKey](jointkey/littlemcp.md)
  A key associated with ring finger’s metacarpophalangeal (MCP) joint in a hand pose.
- [static let littlePIP: JointKey](jointkey/littlepip.md)
  A key associated with ring finger’s proximal interphalangeal (PIP) joint in a hand pose.
- [static let littleTip: JointKey](jointkey/littletip.md)
  A key associated with ring finger tip joint in a hand pose.
### Getting middle finger properties
- [static let middleDIP: JointKey](jointkey/middledip.md)
  A key associated with middle finger’s distal interphalangeal (DIP) joint in a hand pose.
- [static let middleMCP: JointKey](jointkey/middlemcp.md)
  A key associated with middle finger’s metacarpophalangeal (MCP) joint in a hand pose.
- [static let middlePIP: JointKey](jointkey/middlepip.md)
  A key associated with middle finger’s proximal interphalangeal (PIP) joint in a hand pose.
- [static let middleTip: JointKey](jointkey/middletip.md)
  A key associated with middle finger tip joint in a hand pose.
### Getting ring finger properties
- [static let ringDIP: JointKey](jointkey/ringdip.md)
  A key associated with ring finger’s distal interphalangeal (DIP) joint in a hand pose.
- [static let ringMCP: JointKey](jointkey/ringmcp.md)
  A key associated with ring finger’s metacarpophalangeal (MCP) joint in a hand pose.
- [static let ringPIP: JointKey](jointkey/ringpip.md)
  A key associated with ring finger’s proximal interphalangeal (PIP) joint in a hand pose.
- [static let ringTip: JointKey](jointkey/ringtip.md)
  A key associated with ring finger tip joint in a hand pose.
### Getting thumb properties
- [static let thumbCMC: JointKey](jointkey/thumbcmc.md)
  A key associated with thumb carpometacarpal (CMC) joint in a hand pose.
- [static let thumbIP: JointKey](jointkey/thumbip.md)
  A key associated with thumb interphalangeal (IP) joint in a hand pose.
- [static let thumbMP: JointKey](jointkey/thumbmp.md)
  A key associated with thumb metacarpophalangeal (MP) joint in a hand pose.
- [static let thumbTip: JointKey](jointkey/thumbtip.md)
  A key associated with thumb tip joint in a hand pose.
### Getting wrist properties
- [static let leftWrist: JointKey](jointkey/leftwrist.md)
  A key associated with left wrist joint in a body pose.
- [static let rightWrist: JointKey](jointkey/rightwrist.md)
  A key associated with right wrist joint in a body pose.
- [static let wrist: JointKey](jointkey/wrist.md)
  A key associated with hand wrist joint in a hand pose.
### Getting neck and shoulder properties
- [static let neck: JointKey](jointkey/neck.md)
  A key associated with neck joint in a body pose.
- [static let leftShoulder: JointKey](jointkey/leftshoulder.md)
  A key associated with left shoulder joint in a body pose.
- [static let rightShoulder: JointKey](jointkey/rightshoulder.md)
  A key associated with right shoulder joint in a body pose.
### Getting hip, knee, and ankle properties
- [static let leftHip: JointKey](jointkey/lefthip.md)
  A key associated with left hip joint in a body pose.
- [static let leftKnee: JointKey](jointkey/leftknee.md)
  A key associated with left knee joint in a body pose.
- [static let rightHip: JointKey](jointkey/righthip.md)
  A key associated with right hip joint in a body pose.
- [static let rightKnee: JointKey](jointkey/rightknee.md)
  A key associated with right knee joint in a body pose.
- [static let leftAnkle: JointKey](jointkey/leftankle.md)
  A key associated with left ankle joint in a body pose.
- [static let rightAnkle: JointKey](jointkey/rightankle.md)
  A key associated with right ankle joint in a body pose.
### Getting root and raw Properties
- [static let root: JointKey](jointkey/root.md)
  A key associated with root joint in a body pose.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Counting human body action repetitions in a live video feed](counting-human-body-action-repetitions-in-a-live-video-feed.md)
  Use Create ML Components to analyze a series of video frames and count a person’s repetitive or periodic body movements.
- [struct Pose](pose.md)
  A pose that contains joint keypoints from a person, a hand, or a combination.
- [struct JointPoint](jointpoint.md)
  A joint in a pose that contains a location and scoring information.
- [struct PoseSelector](poseselector.md)
  A transformer that selects one pose from an array of poses.
- [enum PoseSelectionStrategy](poseselectionstrategy.md)
  Pose selection strategy.
- [struct JointsSelector](jointsselector.md)
  Joints selector from a pose.
- [struct HumanBodyPoseExtractor](humanbodyposeextractor.md)
  The human body pose image feature extractor.
- [struct HumanHandPoseExtractor](humanhandposeextractor.md)
  The human hand pose image feature extractor.
- [struct HumanBodyActionCounter](humanbodyactioncounter.md)
  A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.
- [struct HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
  A human body action period predictor transformer that takes window of poses and produces a window of predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/jointkey)*