# transform

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a new affine transform initialized to the identity matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```objc
+ (NSAffineTransform *) transform;
```

## Return Value

A new identity transform object. This matrix transforms any point to the same point.

## See Also

### Related Documentation
- [Cocoa Drawing Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
### Creating an Affine Transform
- [init()](./init%28%29.md)
  Initializes an affine transform matrix to the identity matrix.
- [convenience init(transform: NSAffineTransform)](./init%28transform%29.md)
  Initializes the receiver’s matrix using another transform object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transform)*