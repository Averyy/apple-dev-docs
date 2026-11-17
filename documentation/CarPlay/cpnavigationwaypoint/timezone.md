# timeZone

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The timezone for the waypoint.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var timeZone: TimeZone? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSTimeZone * timeZone;
```

## See Also

### Getting the waypoint location
- [var centerPoint: CPLocationCoordinate3D](./centerpoint.md)
  centerPoint is a CPLocationCoordinate3D representing the primary coordinate location of the waypoint.
- [var entryPoints: [CPLocationCoordinate3D]](./entrypoints-obhb.md)
- [var locationThreshold: Measurement<UnitLength>?](./locationthreshold.md)
  locationThreshold is the maximum distance in meters from the centerPoint used to determine if a destination is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/timezone)*