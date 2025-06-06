# GLKMathUnproject(_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func

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

#### Return Value

The projected point in object space.

## Parameters

- `window`: The point in window coordinates.
- `model`: A modelview transformation matrix.
- `projection`: A projection matrix.
- `viewport`: A pointer to an array of four integer values. The first pair of values represent the window coordinates of the viewport’s bottom left corner. The second pair of values represent the width and height of the view port.
- `success`: Upon return, contains   if the function completed successfully, otherwise it contains  . Pass   if you do not want error information.

## See Also

- [func GLKMathProject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>) -> GLKVector3](glkmathproject(_:_:_:_:).md)
  Projects a point in object space into the window coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmathunproject(_:_:_:_:_:))*