# init(from:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates a pose from a dictionary of joint keypoints.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(from points: [JointKey : JointPoint])
```

**Other overloads**:

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `points`: A dictionary of pose joint keypoints, where keys are joint names and values are joint points.

## See Also

### Creating a pose
- [init(VNRecognizedPointsObservation) throws](./init%28_%29.md)
  Creates a pose from a body or hand pose observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pose/init(from:)-8rvl5)*