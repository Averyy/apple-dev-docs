# convertTime(_:to:)

**Framework**: Core Animation  
**Kind**: method

Converts the time interval from the receiver’s time space to the specified layer’s time space

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func convertTime(_ t: CFTimeInterval, to l: CALayer?) -> CFTimeInterval
```

#### Return Value

The time interval converted to the time space of `layer`.

#### Discussion

The following code shows the creation of two layers, `layer` and `offsetSlowMoLayer`. `offsetSlowMoLayer` has an offset time of 1 second and its [`speed`](camediatiming/speed.md) is set to `0.5`.  The last line converts and prints a time interval of 0.5 seconds converted from the time space of `layer` to the time space of `offsetSlowMoLayer`.

```swift
let layer = CALayer()
let offsetSlowMoLayer = CALayer()
     
offsetSlowMoLayer.timeOffset = CFTimeInterval(1)
offsetSlowMoLayer.speed = 0.5
     
print(layer.convertTime(CFTimeInterval(0.5), to: offsetSlowMoLayer)) // prints 1.25
```

## Parameters

- `t`: A point specifying a location in the coordinate system of  .
- `l`: The layer into whose time space   is to be converted. The receiver and   and must share a common parent layer.

## See Also

- [func convert(CGPoint, from: CALayer?) -> CGPoint](calayer/convert(_:from:)-8kl76.md)
  Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGPoint, to: CALayer?) -> CGPoint](calayer/convert(_:to:)-7dcke.md)
  Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convert(CGRect, from: CALayer?) -> CGRect](calayer/convert(_:from:)-4kx9l.md)
  Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGRect, to: CALayer?) -> CGRect](calayer/convert(_:to:)-tly5.md)
  Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convertTime(CFTimeInterval, from: CALayer?) -> CFTimeInterval](calayer/converttime(_:from:).md)
  Converts the time interval from the specified layer’s time space to the receiver’s time space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/converttime(_:to:))*