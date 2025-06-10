# HumanBodyActionPeriodPredictor

**Framework**: Create ML Components  
**Kind**: struct

A human body action period predictor transformer that takes window of poses and produces a window of predictions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct HumanBodyActionPeriodPredictor
```

## Topics

### Creating a transformer
- [init()](humanbodyactionperiodpredictor/init.md)
  Creates a human body action period predictor transformer.
### Performing the transformation
- [func applied(to: [Pose], eventHandler: EventHandler?) async throws -> [HumanBodyActionPeriodPredictor.Prediction]](humanbodyactionperiodpredictor/applied(to:eventhandler:).md)
  Predicts human body action periods from an array of poses.
- [HumanBodyActionPeriodPredictor.Input](humanbodyactionperiodpredictor/input.md)
  The input type.
- [HumanBodyActionPeriodPredictor.Output](humanbodyactionperiodpredictor/output.md)
  The output type.
- [HumanBodyActionPeriodPredictor.Prediction](humanbodyactionperiodpredictor/prediction.md)
  A human body action period prediction.
### Default Implementations
- [Transformer Implementations](humanbodyactionperiodpredictor/transformer-implementations.md)

## Relationships

### Conforms To
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
- [struct JointsSelector](jointsselector.md)
  Joints selector from a pose.
- [struct HumanBodyPoseExtractor](humanbodyposeextractor.md)
  The human body pose image feature extractor.
- [struct HumanHandPoseExtractor](humanhandposeextractor.md)
  The human hand pose image feature extractor.
- [struct HumanBodyActionCounter](humanbodyactioncounter.md)
  A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor)*