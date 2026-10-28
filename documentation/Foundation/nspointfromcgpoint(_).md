# NSPointFromCGPoint(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns an `NSPoint` typecast from a `CGPoint`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSPointFromCGPoint(_ cgpoint: CGPoint) -> NSPoint
```

```c
static NSPoint NSPointFromCGPoint(CGPoint cgpoint);
```

## Return Value

An `NSPoint` typecast from a `CGPoint`.

## See Also

### Related Documentation
- [func NSRectFromCGRect(CGRect) -> NSRect](./nsrectfromcgrect%28_%29.md)
  Returns an `NSRect` typecast from a `CGRect`.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.
### Managing Points
- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](./nsequalpoints%28_,_%29.md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](./nsmakepoint%28_,_%29.md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](./nsstringfrompoint%28_%29.md)
  Returns a string representation of a point.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointfromcgpoint(_:))*