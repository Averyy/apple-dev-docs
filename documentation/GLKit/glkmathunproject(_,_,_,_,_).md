# GLKMathUnproject(_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Projects a point in view space into object space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMathUnproject(_ window: GLKVector3, _ model: GLKMatrix4, _ projection: GLKMatrix4, _ viewport: UnsafeMutablePointer<Int32>, _ success: UnsafeMutablePointer<Bool>?) -> GLKVector3
```

```c
GLKVector3 GLKMathUnproject(GLKVector3 window, GLKMatrix4 model, GLKMatrix4 projection, int *viewport, bool *success);
```

## Return Value

The projected point in object space.

## Parameters

- `window`: The point in window coordinates.
- `model`: A modelview transformation matrix.
- `projection`: A projection matrix.
- `viewport`: A pointer to an array of four integer values. The first pair of values represent the window coordinates of the viewport’s bottom left corner. The second pair of values represent the width and height of the view port.
- `success`: Upon return, contains [`true`](../Swift/true.md) if the function completed successfully, otherwise it contains [`false`](../Swift/false.md). Pass `NULL` if you do not want error information.

## See Also

### Projecting Vectors
- [func GLKMathProject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>) -> GLKVector3](./glkmathproject%28_,_,_,_%29.md)
  Projects a point in object space into the window coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmathunproject(_:_:_:_:_:))*