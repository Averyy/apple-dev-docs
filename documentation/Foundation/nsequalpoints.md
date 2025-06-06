# NSEqualPoints(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether two points are equal.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSEqualPoints(_ aPoint: NSPoint, _ bPoint: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the two points `aPoint` and `bPoint` are identical, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func NSMakePoint(Double, Double) -> NSPoint](nsmakepoint(_:_:).md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](nspointfromstring(_:).md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](nsstringfrompoint(_:).md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](nspointfromcgpoint(_:).md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](nspointtocgpoint(_:).md)
  Returns a `CGPoint` typecast from an `NSPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalpoints(_:_:))*