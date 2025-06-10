# program(_:handleError:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate that an error occurred when compiling GLSL source code.

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
optional func program(_ program: SCNProgram, handleError error: any Error)
```

#### Discussion

Examine the `error` parameter for details of the compilation error provided by the GLSL compiler.

## Parameters

- `program`: The program that generated the compilation error.
- `error`: The compilation error that was raised.

## See Also

- [let SCNErrorDomain: String](scnerrordomain.md)
  Identifies an error type defined by the SceneKit framework.
- [SceneKit Error Codes](1409723-scenekit-error-codes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/program(_:handleerror:))*