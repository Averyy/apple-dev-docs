# primaryAngle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A value that represents the angle the framework highlights if this lane is preferred or good.

**Availability**:
- iOS 17.4+ - Deprecated in 18.0
- iPadOS 17.4+ - Deprecated in 18.0
- Mac Catalyst 17.4+ - Deprecated in 18.0

> **Deprecated**: Use highlightedAngle to get value, use -[CPLane initAngles:highlightedAngle:isPreferred:] to create a CPLane with highlightedAngle set

## Declaration

```swift
var primaryAngle: Measurement<UnitAngle> { get set }
```

```objc
@property (nonatomic, strong) NSMeasurement<NSUnitAngle *> * primaryAngle;
```

#### Discussion

If `primaryAngle` is present it can’t be included in [`secondaryAngles`](./secondaryangles.md).

## See Also

### Properties
- [var secondaryAngles: [Measurement<UnitAngle>]](./secondaryangles.md)
  A list of the remaining angles of this lane guidance.
- [var status: CPLaneStatus](./status.md)
  A value that describes the lane’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane/primaryangle)*