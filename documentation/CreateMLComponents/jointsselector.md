# JointsSelector

**Framework**: Create ML Components  
**Kind**: struct

Joints selector from a pose.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct JointsSelector
```

## Topics

### Creating a selector
- [init(ignoredJoints: [JointKey])](jointsselector/init(ignoredjoints:).md)
  Creates a joint selector transformer using a list of joint keys to be ignored.
- [init(selectedJoints: [JointKey])](jointsselector/init(selectedjoints:).md)
  Creates a joint selector transformer using a list of joint keys to be selected.
### Getting the properties
- [var ignoredJoints: [JointKey]?](jointsselector/ignoredjoints.md)
  A list of joint keys to be ignored.
- [var selectedJoints: [JointKey]?](jointsselector/selectedjoints.md)
  A list of joint keys to be selected.
### Performing the selector
- [func applied(to: Pose, eventHandler: EventHandler?) -> Pose](jointsselector/applied(to:eventhandler:).md)
  Select joints to be included in the pose. Ignored joints will be reset to zero in all fields.
### Type Aliases
- [JointsSelector.Input](jointsselector/input.md)
  The input type.
- [JointsSelector.Output](jointsselector/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](jointsselector/customdebugstringconvertible-implementations.md)
- [Transformer Implementations](jointsselector/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)

## See Also

- [Counting human body action repetitions in a live video feed](counting_human_body_action_repetitions_in_a_live_video_feed.md)
  Use Create ML Components to analyze a series of video frames and count a person’s repetitive or periodic body movements.
- [struct Pose](pose.md)
  A pose that contains joint keypoints from a person, a hand, or a combination.
- [struct JointKey](jointkey.md)
  A key that uniquely identifies a joint.
- [struct JointPoint](jointpoint.md)
  A joint in a pose that contains a location and scoring information.
- [struct PoseSelector](poseselector.md)
  A transformer that selects one pose from an array of poses.
- [enum PoseSelectionStrategy](poseselectionstrategy.md)
  Pose selection strategy.
- [struct HumanBodyPoseExtractor](humanbodyposeextractor.md)
  The human body pose image feature extractor.
- [struct HumanHandPoseExtractor](humanhandposeextractor.md)
  The human hand pose image feature extractor.
- [struct HumanBodyActionCounter](humanbodyactioncounter.md)
  A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.
- [struct HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
  A human body action period predictor transformer that takes window of poses and produces a window of predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/jointsselector)*