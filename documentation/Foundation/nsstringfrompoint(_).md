# NSStringFromPoint(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a string representation of a point.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSStringFromPoint(_ aPoint: NSPoint) -> String
```

```c
extern NSString *NSStringFromPoint(NSPoint aPoint);
```

## Return Value

A string of the form “{a, b}”, where a and b are the x and y coordinates of `aPoint`.

## Parameters

- `aPoint`: A point structure.

## See Also

### Managing Points
- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](./nsequalpoints%28_,_%29.md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](./nsmakepoint%28_,_%29.md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfrompoint(_:))*