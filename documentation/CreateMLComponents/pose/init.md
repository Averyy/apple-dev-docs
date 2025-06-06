# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates a pose from a body or hand pose observation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(_ observation: VNRecognizedPointsObservation) throws
```

## Parameters

- `observation`: Recognized points observation that comes from either a body pose or hand pose request.

## See Also

- [init(from: [JointKey : JointPoint])](pose/init(from:)-8rvl5.md)
  Creates a pose from a dictionary of joint keypoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pose/init(_:))*