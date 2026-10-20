# program(_:handleError:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that an error occurred when compiling GLSL source code.

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
optional func program(_ program: SCNProgram, handleError error: any Error)
```

```objc
- (void) program:(SCNProgram *) program handleError:(NSError *) error;
```

#### Discussion

Examine the `error` parameter for details of the compilation error provided by the GLSL compiler.

## Parameters

- `program`: The program that generated the compilation error.
- `error`: The compilation error that was raised.

## See Also

### Handling Shader Compilation Errors
- [let SCNErrorDomain: String](../scnerrordomain.md)
  Identifies an error type defined by the SceneKit framework.
- [SceneKit Error Codes](../api-1409723-scenekit-error-codes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/program(_:handleerror:))*