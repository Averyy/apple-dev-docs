# GLKMathProject(_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Projects a point in object space into the window coordinate system.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMathProject(_ object: GLKVector3, _ model: GLKMatrix4, _ projection: GLKMatrix4, _ viewport: UnsafeMutablePointer<Int32>) -> GLKVector3
```

```c
GLKVector3 GLKMathProject(GLKVector3 object, GLKMatrix4 model, GLKMatrix4 projection, int *viewport);
```

## Return Value

The projected point in window coordinates.

## Parameters

- `object`: The point in object space.
- `model`: A modelview transformation matrix.
- `projection`: A projection matrix.
- `viewport`: A pointer to an array of four integer values. The first pair of values represent the window coordinates of the viewport’s bottom left corner. The second pair of values represent the width and height of the view port.

## See Also

### Projecting Vectors
- [func GLKMathUnproject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Bool>?) -> GLKVector3](./glkmathunproject%28_,_,_,_,_%29.md)
  Projects a point in view space into object space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmathproject(_:_:_:_:))*