# pose

**Framework**: Group Activities  
**Kind**: property

The position and rotation of the participant – at the time the system coordinator state last changed.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
let pose: Pose3D?
```

#### Discussion

You should use this property instead of the `seat/pose` property when you want to position something relative to the participant assigned to this seat, and not the seat itself.

The system will always try to place a participant in their seat at the time of assignment so in many cases both poses will be the same. But if the system is unable to place a participant in their seat, they may be different. For example, if participants in your SharePlay activity are Nearby with each other, the system is unable to move them physically in space.

> ❗ **Important**:  This is not a dynamically updating value. It is the pose of the participant  and does not reflect the participant’s pose in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate/pose)*