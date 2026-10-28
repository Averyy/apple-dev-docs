# init(name:)

**Framework**: Core Animation  
**Kind**: init  
**Role**: Initializer

Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: CAMediaTimingFunctionName)
```

```objc
+ (instancetype) functionWithName:(CAMediaTimingFunctionName) name;
```

## Return Value

A new instance of `CAMediaTimingFunction` with the timing function specified by `name`.

## Parameters

- `name`: The timing function to use as specified in [Predefined Timing Functions](../predefined-timing-functions.md).

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Creating Timing Functions
- [init(controlPoints: Float, Float, Float, Float)](./init%28controlpoints,_,_,_%29.md)
  Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.
- [+ functionWithControlPoints::::](./functionwithcontrolpoints____.md)
  Creates and returns a new instance of `CAMediaTimingFunction` timing function modeled as a cubic Bézier curve using the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/init(name:))*