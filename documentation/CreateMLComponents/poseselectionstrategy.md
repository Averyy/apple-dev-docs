# PoseSelectionStrategy

**Framework**: Create ML Components  
**Kind**: enum

Pose selection strategy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum PoseSelectionStrategy
```

## Topics

### Selection strategies
- [PoseSelectionStrategy.maximumBoundingBoxArea](poseselectionstrategy/maximumboundingboxarea.md)
  The strategy to choose a pose with the maximum bounding box area.
- [PoseSelectionStrategy.highestJointLocation](poseselectionstrategy/highestjointlocation.md)
  The strategy to choose a pose where a joint in it has the higest y coordinate location.
- [PoseSelectionStrategy.leftmostJointLocation](poseselectionstrategy/leftmostjointlocation.md)
  The strategy to choose a pose where a joint in it has the leftmost x coordinate location.
- [PoseSelectionStrategy.lowestJointLocation](poseselectionstrategy/lowestjointlocation.md)
  The strategy to choose a pose where a joint in it has the lowest y coordinate location.
- [PoseSelectionStrategy.rightmostJointLocation](poseselectionstrategy/rightmostjointlocation.md)
  The strategy to choose a pose where a joint in it has the leftmost x coordinate location.
### Operators
- [static func == (PoseSelectionStrategy, PoseSelectionStrategy) -> Bool](poseselectionstrategy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](poseselectionstrategy/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](poseselectionstrategy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](poseselectionstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/poseselectionstrategy)*