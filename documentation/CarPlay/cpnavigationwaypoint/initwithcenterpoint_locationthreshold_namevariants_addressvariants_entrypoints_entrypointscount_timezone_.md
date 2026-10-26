# initWithCenterPoint:locationThreshold:nameVariants:addressVariants:entryPoints:entryPointsCount:timeZone:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Initialize a CPNavigationWaypoint object with a center point, location threshold, optional name and name variants, optional long address and short address, optional entry points, and a timezone.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```objc
- (instancetype) initWithCenterPoint:(CPLocationCoordinate3D) centerPoint locationThreshold:(NSMeasurement<NSUnitLength *> *) locationThreshold nameVariants:(NSArray<NSString *> *) nameVariants addressVariants:(NSArray<NSString *> *) addressVariants entryPoints:(CPLocationCoordinate3D *) entryPoints entryPointsCount:(NSUInteger) entryPointsCount timeZone:(NSTimeZone *) timeZone;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint/initwithcenterpoint:locationthreshold:namevariants:addressvariants:entrypoints:entrypointscount:timezone:)*