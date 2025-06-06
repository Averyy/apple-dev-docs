# EAGLGetVersion(_:_:)

**Framework**: OpenGL ES  
**Kind**: func

Retrieves the version information for the EAGL implementation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
func EAGLGetVersion(_ major: UnsafeMutablePointer<UInt32>, _ minor: UnsafeMutablePointer<UInt32>)
```

#### Discussion

If `major` and `minor` parameters are not `nil`, they return the major and minor version number of the EAGL implementation, respectively.

## Parameters

- `major`: On output, the major version of the EAGL implementation.
- `minor`: On output, the minor version of the EAGL implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglgetversion(_:_:))*