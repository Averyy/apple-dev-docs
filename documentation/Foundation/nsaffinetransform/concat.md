# concat()

**Framework**: Foundation  
**Kind**: method

Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func concat()
```

#### Discussion

Concatenation is performed by matrix multiplication—see Manipulating Transform Values.

If this method is invoked from within an `NSView`[`draw(_:)`](https://developer.apple.com/documentation/AppKit/NSView/draw(_:)) method, then the current transformation matrix is an accumulation of the screen, window, and any superview’s transformation matrices. Invoking this method defines a new user coordinate system whose coordinates are mapped into the former coordinate system according to the receiver’s transformation matrix. To undo the concatenation, you must invert the receiver’s matrix and invoke this method again.

## See Also

- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.
- [func set()](nsaffinetransform/set.md)
  Sets the current transformation matrix to the receiver’s transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/concat())*