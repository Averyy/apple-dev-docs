# transform(_:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a new [`NSBezierPath`](https://developer.apple.com/documentation/AppKit/NSBezierPath) object with each point in the given path transformed by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func transform(_ path: NSBezierPath) -> NSBezierPath
```

#### Discussion

The original `NSBezierPath` object is not modified.

## Parameters

- `path`: An object representing the bezier path to be used in the transformation.

## See Also

- [func transform(NSPoint) -> NSPoint](nsaffinetransform/transform(_:)-41p16.md)
  Applies the receiver’s transform to the specified point and returns the result.
- [func transform(NSSize) -> NSSize](nsaffinetransform/transform(_:)-5r6ol.md)
  Applies the receiver’s transform to the specified size and returns the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-6z1xo)*