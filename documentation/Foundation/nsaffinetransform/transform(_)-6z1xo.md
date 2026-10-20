# transform(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func transform(_ path: NSBezierPath) -> NSBezierPath
```

```objc
- (NSBezierPath *) transformBezierPath:(NSBezierPath *) path;
```

#### Discussion

The original `NSBezierPath` object is not modified.

## Parameters

- `path`: An object representing the bezier path to be used in the transformation.

## See Also

### Transforming Data and Objects
- [func transform(NSPoint) -> NSPoint](./transform%28_%29-41p16.md)
  Applies the receiver’s transform to the specified point and returns the result.
- [func transform(NSSize) -> NSSize](./transform%28_%29-5r6ol.md)
  Applies the receiver’s transform to the specified size and returns the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-6z1xo)*