# HumanBodyActionCounter

**Framework**: Create ML Components  
**Kind**: struct

A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct HumanBodyActionCounter
```

## Topics

### Creating a transformer
- [init()](humanbodyactioncounter/init.md)
  Creates a human body action counter.
### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> HumanBodyActionCounter.OutputSequence](humanbodyactioncounter/applied(to:eventhandler:).md)
  Predicts cumulative human body action counts from a sequence of human body pose windows.
- [HumanBodyActionCounter.Input](humanbodyactioncounter/input.md)
  The input type.
- [HumanBodyActionCounter.Output](humanbodyactioncounter/output.md)
  The output type.
- [HumanBodyActionCounter.CumulativeSumSequence](humanbodyactioncounter/cumulativesumsequence.md)
  Cumulative human body action count sequence.
- [HumanBodyActionCounter.OutputSequence](humanbodyactioncounter/outputsequence.md)
  The output async sequence type.
### Default Implementations
- [TemporalTransformer Implementations](humanbodyactioncounter/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)

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
- [struct HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
  A human body action period predictor transformer that takes window of poses and produces a window of predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter)*