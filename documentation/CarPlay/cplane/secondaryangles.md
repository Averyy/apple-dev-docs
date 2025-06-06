# secondaryAngles

**Framework**: CarPlay  
**Kind**: property

A list of the remaining angles of this lane guidance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var secondaryAngles: [Measurement<UnitAngle>] { get set }
```

##### Discussion

This doesn’t include the `primaryAngle`.

## See Also

- [var primaryAngle: Measurement<UnitAngle>](cplane/primaryangle.md)
  A value that represents the angle the framework highlights if this lane is preferred or good.
- [var status: CPLaneStatus](cplane/status.md)
  A value that describes the lane’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane/secondaryangles)*