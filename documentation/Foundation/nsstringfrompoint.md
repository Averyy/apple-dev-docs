# NSStringFromPoint(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string representation of a point.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSStringFromPoint(_ aPoint: NSPoint) -> String
```

#### Return Value

A string of the form “{a, b}”, where a and b are the x and y coordinates of `aPoint`.

## Parameters

- `aPoint`: A point structure.

## See Also

- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](nsequalpoints(_:_:).md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](nsmakepoint(_:_:).md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](nspointfromstring(_:).md)
  Returns a point from a text-based representation.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](nspointfromcgpoint(_:).md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](nspointtocgpoint(_:).md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfrompoint(_:))*