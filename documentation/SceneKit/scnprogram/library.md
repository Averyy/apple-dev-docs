# library

**Framework**: SceneKit  
**Kind**: property

The Metal shader library containing shader functions to be used by this program.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var library: (any MTLLibrary)? { get set }
```

#### Discussion

If this property’s value is nil (the default), SceneKit loads shader functions from the default Metal library. Change this value if you have compiled a separate `.metallib` file for the shader functions you wish to use.

## See Also

- [func makeDefaultLibrary() -> (any MTLLibrary)?](../Metal/MTLDevice/makeDefaultLibrary.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [var vertexFunctionName: String?](scnprogram/vertexfunctionname.md)
  The name of the vertex shader function to load from a Metal shader library.
- [var fragmentFunctionName: String?](scnprogram/fragmentfunctionname.md)
  The name of the fragment shader function to load from a Metal shader library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/library)*