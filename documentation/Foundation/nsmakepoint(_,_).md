# NSMakePoint(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Creates a new `NSPoint` from the specified values.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSMakePoint(_ x: Double, _ y: Double) -> NSPoint
```

```c
static NSPoint NSMakePoint(CGFloat x, CGFloat y);
```

## Return Value

An `NSPoint` having the coordinates `x` and `y`.

## See Also

### Managing Points
- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](./nsequalpoints%28_,_%29.md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](./nsstringfrompoint%28_%29.md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmakepoint(_:_:))*