# NSPointFromString(_:)

**Framework**: Foundation  
**Kind**: func

Returns a point from a text-based representation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSPointFromString(_ aString: String) -> NSPoint
```

#### Return Value

If `aString` is of the form “{x, y}” an `NSPoint` structure that uses x and y as the x and y coordinates, in that order.

#### Discussion

If `aString` only contains a single number, it is used as the x coordinate. If `aString` does not contain any numbers, returns an `NSPoint` object whose x and y coordinates are both 0.

## Parameters

- `aString`: A string of the form “{x, y}”.

## See Also

- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](nsequalpoints(_:_:).md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](nsmakepoint(_:_:).md)
  Creates a new `NSPoint` from the specified values.
- [func NSStringFromPoint(NSPoint) -> String](nsstringfrompoint(_:).md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](nspointfromcgpoint(_:).md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](nspointtocgpoint(_:).md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointfromstring(_:))*