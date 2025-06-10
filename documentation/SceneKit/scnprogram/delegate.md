# delegate

**Framework**: SceneKit  
**Kind**: property

The delegate of the program object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any SCNProgramDelegate)? { get set }
```

#### Discussion

An [`SCNProgram`](scnprogram.md) object sends delegate messages if errors occur when compiling GLSL source code.

## See Also

- [protocol SCNProgramDelegate](scnprogramdelegate.md)
  The interface for tracking errors that occur when compiling shader source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/delegate)*