# initWithMapItem:locationThreshold:entryPoints:entryPointsCount:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Initialize a CPNavigationWaypoint object from an MKMapItem with a location threshold and optional entry points.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```objc
- (instancetype) initWithMapItem:(MKMapItem *) mapItem locationThreshold:(NSMeasurement<NSUnitLength *> *) locationThreshold entryPoints:(CPLocationCoordinate3D *) entryPoints entryPointsCount:(NSUInteger) entryPointsCount;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/initwithmapitem:locationthreshold:entrypoints:entrypointscount:)*