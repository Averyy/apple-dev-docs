# centerPoint

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

centerPoint is a CPLocationCoordinate3D representing the primary coordinate location of the waypoint.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var centerPoint: CPLocationCoordinate3D { get }
```

```objc
@property (nonatomic, readonly) CPLocationCoordinate3D centerPoint;
```

## See Also

### Getting the waypoint location
- [var entryPoints: [CPLocationCoordinate3D]](./entrypoints-obhb.md)
- [var locationThreshold: Measurement<UnitLength>?](./locationthreshold.md)
  locationThreshold is the maximum distance in meters from the centerPoint used to determine if a destination is valid.
- [var timeZone: TimeZone?](./timezone.md)
  The timezone for the waypoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/centerpoint)*