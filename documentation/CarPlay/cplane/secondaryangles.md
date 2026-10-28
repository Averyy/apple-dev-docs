# secondaryAngles

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A list of the remaining angles of this lane guidance.

**Availability**:
- iOS 17.4+ - Deprecated in 18.0
- iPadOS 17.4+ - Deprecated in 18.0
- Mac Catalyst 17.4+ - Deprecated in 18.0

> **Deprecated**: Use angles to get value, Use -[CPLane initWithAngles:] or -[CPLane initAngles:highlightedAngle:isPreferred:] to create a CPLane with angles

## Declaration

```swift
var secondaryAngles: [Measurement<UnitAngle>] { get set }
```

```objc
@property (nonatomic, strong) NSArray<NSMeasurement<NSUnitAngle *> *> * secondaryAngles;
```

### Discussion

This doesn’t include the `primaryAngle`.

## See Also

### Properties
- [var primaryAngle: Measurement<UnitAngle>](./primaryangle.md)
  A value that represents the angle the framework highlights if this lane is preferred or good.
- [var status: CPLaneStatus](./status.md)
  A value that describes the lane’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane/secondaryangles)*