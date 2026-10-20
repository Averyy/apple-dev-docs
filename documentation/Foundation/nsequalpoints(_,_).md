# NSEqualPoints(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two points are equal.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSEqualPoints(_ aPoint: NSPoint, _ bPoint: NSPoint) -> Bool
```

```c
extern BOOL NSEqualPoints(NSPoint aPoint, NSPoint bPoint);
```

#### Return Value

[`true`](../Swift/true.md) if the two points `aPoint` and `bPoint` are identical, otherwise [`false`](../Swift/false.md).

## See Also

### Managing Points
- [func NSMakePoint(Double, Double) -> NSPoint](./nsmakepoint%28_,_%29.md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](./nsstringfrompoint%28_%29.md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalpoints(_:_:))*