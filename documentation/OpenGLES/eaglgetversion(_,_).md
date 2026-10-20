# EAGLGetVersion(_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

Retrieves the version information for the EAGL implementation.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func EAGLGetVersion(_ major: UnsafeMutablePointer<UInt32>, _ minor: UnsafeMutablePointer<UInt32>)
```

```c
extern void EAGLGetVersion(unsigned int *major, unsigned int *minor);
```

#### Discussion

If `major` and `minor` parameters are not `nil`, they return the major and minor version number of the EAGL implementation, respectively.

## Parameters

- `major`: On output, the major version of the EAGL implementation.
- `minor`: On output, the minor version of the EAGL implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglgetversion(_:_:))*