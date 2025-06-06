# PoseSelector

**Framework**: Create ML Components  
**Kind**: struct

A transformer that selects one pose from an array of poses.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct PoseSelector
```

## Topics

### Creating a selector
- [init()](poseselector/init.md)
  Creates a pose selector.
- [init(strategy: PoseSelectionStrategy)](poseselector/init(strategy:).md)
  Creates a pose selector.
- [init(strategy: PoseSelectionStrategy, confidenceThreshold: Float)](poseselector/init(strategy:confidencethreshold:).md)
  Creates a pose selector.
### Getting the properties
- [var confidenceThreshold: Float](poseselector/confidencethreshold.md)
  A threshold confidence between 0 to 1 for the joints to be considered valid in pose selection. The default value is 0.2.
- [var strategy: PoseSelectionStrategy](poseselector/strategy.md)
  Pose selection strategy.
### Performing the transformation
- [func applied(to: [Pose], eventHandler: EventHandler?) -> Pose](poseselector/applied(to:eventhandler:).md)
  Select a pose if multiple poses are detected on the same frame.
### Type Aliases
- [PoseSelector.Input](poseselector/input.md)
  The input type.
- [PoseSelector.Output](poseselector/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](poseselector/customdebugstringconvertible-implementations.md)
- [Transformer Implementations](poseselector/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/poseselector)*