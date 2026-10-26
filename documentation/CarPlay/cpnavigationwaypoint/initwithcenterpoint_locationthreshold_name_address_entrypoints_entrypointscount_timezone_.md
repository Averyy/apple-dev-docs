# initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:timeZone:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Initialize a CPNavigationWaypoint object with a center point, location threshold, optional name and address, optional entry points, and a timezone.

**Availability**:
- iOS 26.4+ - Deprecated in 27.0
- iPadOS 26.4+ - Deprecated in 27.0
- Mac Catalyst 26.4+ - Deprecated in 27.0

## Declaration

```objc
- (instancetype) initWithCenterPoint:(CPLocationCoordinate3D) centerPoint locationThreshold:(NSMeasurement<NSUnitLength *> *) locationThreshold name:(NSString *) name address:(NSString *) address entryPoints:(CPLocationCoordinate3D *) entryPoints entryPointsCount:(NSUInteger) entryPointsCount timeZone:(NSTimeZone *) timeZone;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/initwithcenterpoint:locationthreshold:name:address:entrypoints:entrypointscount:timezone:)*