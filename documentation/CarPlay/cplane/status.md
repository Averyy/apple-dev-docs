# status

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A value that describes the lane’s status.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var status: CPLaneStatus { get set }
```

```objc
@property (nonatomic, assign) CPLaneStatus status;
```

## Discussion

One of the [`CPLaneStatus`](../cplanestatus.md) values that describes the lane’s status.

## See Also

### Properties
- [var primaryAngle: Measurement<UnitAngle>](./primaryangle.md)
  A value that represents the angle the framework highlights if this lane is preferred or good.
- [var secondaryAngles: [Measurement<UnitAngle>]](./secondaryangles.md)
  A list of the remaining angles of this lane guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplane/status)*