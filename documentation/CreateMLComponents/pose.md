# Pose

**Framework**: Create ML Components  
**Kind**: struct

A pose that contains joint keypoints from a person, a hand, or a combination.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Pose
```

## Topics

### Creating a pose
- [init(VNRecognizedPointsObservation) throws](pose/init(_:).md)
  Creates a pose from a body or hand pose observation.
- [init(from: [JointKey : JointPoint])](pose/init(from:)-8rvl5.md)
  Creates a pose from a dictionary of joint keypoints.
### Getting the key points
- [var keypoints: [JointKey : JointPoint]](pose/keypoints.md)
  A dictionary of all keypoints in the pose
### Computing the bounding box
- [func boundingBoxArea(confidenceThreshold: Float) -> Float](pose/boundingboxarea(confidencethreshold:).md)
  Computes the bounding box area of the pose.
### Default Implementations
- [Decodable Implementations](pose/decodable-implementations.md)
- [Encodable Implementations](pose/encodable-implementations.md)
- [Equatable Implementations](pose/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Counting human body action repetitions in a live video feed](counting_human_body_action_repetitions_in_a_live_video_feed.md)
  Use Create ML Components to analyze a series of video frames and count a person’s repetitive or periodic body movements.
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
- [struct HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
  A human body action period predictor transformer that takes window of poses and produces a window of predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pose)*