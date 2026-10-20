# delegate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the program object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
unowned(unsafe) var delegate: (any SCNProgramDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<SCNProgramDelegate> delegate;
```

#### Discussion

An [`SCNProgram`](../scnprogram.md) object sends delegate messages if errors occur when compiling GLSL source code.

## See Also

### Providing a Delegate Object
- [protocol SCNProgramDelegate](../scnprogramdelegate.md)
  The interface for tracking errors that occur when compiling shader source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/delegate)*