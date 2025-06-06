# primaryAngle

**Framework**: CarPlay  
**Kind**: property

A value that represents the angle the framework highlights if this lane is preferred or good.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var primaryAngle: Measurement<UnitAngle> { get set }
```

#### Discussion

If `primaryAngle` is present it can’t be included in [`secondaryAngles`](cplane/secondaryangles.md).

## See Also

- [var secondaryAngles: [Measurement<UnitAngle>]](cplane/secondaryangles.md)
  A list of the remaining angles of this lane guidance.
- [var status: CPLaneStatus](cplane/status.md)
  A value that describes the lane’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane/primaryangle)*