# NSPointToCGPoint(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a `CGPoint` typecast from an `NSPoint`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSPointToCGPoint(_ nspoint: NSPoint) -> CGPoint
```

```c
static CGPoint NSPointToCGPoint(NSPoint nspoint);
```

## Return Value

A `CGPoint` typecast from an `NSPoint`.

## See Also

### Related Documentation
- [func NSRectToCGRect(NSRect) -> CGRect](./nsrecttocgrect%28_%29.md)
  Returns a `CGRect` typecast from an `NSRect`.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.
### Managing Points
- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](./nsequalpoints%28_,_%29.md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](./nsmakepoint%28_,_%29.md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](./nsstringfrompoint%28_%29.md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointtocgpoint(_:))*