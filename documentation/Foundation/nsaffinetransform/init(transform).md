# init(transform:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver’s matrix using another transform object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

*Mac Catalyst*

```swift
convenience init(transform: NSAffineTransform)
```

*macOS*

```swift
convenience init(transform: AffineTransform)
```

```objc
- (instancetype) initWithTransform:(NSAffineTransform *) transform;
```

## Return Value

A new transform object initialized with the matrix values of `aTransform`.

## Parameters

- `transform`: The transform object whose matrix values should be copied to this object.

## See Also

### Creating an Affine Transform
- [init()](./init%28%29.md)
  Initializes an affine transform matrix to the identity matrix.
### Related Documentation
- [+ transform](./transform.md)
  Creates a new affine transform initialized to the identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/init(transform:))*