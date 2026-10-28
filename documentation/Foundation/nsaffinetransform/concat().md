# concat()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func concat()
```

```objc
- (void) concat;
```

## Discussion

Concatenation is performed by matrix multiplication—see Manipulating Transform Values.

If this method is invoked from within an `NSView`[`draw(_:)`](../../AppKit/nsview/draw%28_%29.md) method, then the current transformation matrix is an accumulation of the screen, window, and any superview’s transformation matrices. Invoking this method defines a new user coordinate system whose coordinates are mapped into the former coordinate system according to the receiver’s transformation matrix. To undo the concatenation, you must invert the receiver’s matrix and invoke this method again.

## See Also

### Related Documentation
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.
### Setting and Building the Current Transformation Matrix
- [func set()](./set%28%29.md)
  Sets the current transformation matrix to the receiver’s transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/concat())*