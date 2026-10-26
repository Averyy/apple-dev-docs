# initWithCenter:radius:

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Creates a new circular geographic condition with the center point and radius you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
- (instancetype) initWithCenter:(CLLocationCoordinate2D) center radius:(CLLocationDistance) radius;
```

#### Return Value

Returns an instance of `CLCircularGeographicCondition` with the specified center coordinate and radius.

## Parameters

- `center`: The center of the circular geographic condition.
- `radius`: The radius of the circular geographic condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcirculargeographiccondition/initwithcenter:radius:)*