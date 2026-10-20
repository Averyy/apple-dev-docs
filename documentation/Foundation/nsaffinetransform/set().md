# set()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the current transformation matrix to the receiver’s transformation matrix.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func set()
```

```objc
- (void) set;
```

#### Discussion

The current transformation is stored in the current graphics context and is applied to subsequent drawing operations. You should use this method sparingly because it removes the existing transformation matrix, which is an accumulation of transformation matrices for the screen, window, and any superviews. Instead use the [`concat()`](./concat%28%29.md) method to add this transformation matrix to the current transformation matrix.

## See Also

### Setting and Building the Current Transformation Matrix
- [func concat()](./concat%28%29.md)
  Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/set())*