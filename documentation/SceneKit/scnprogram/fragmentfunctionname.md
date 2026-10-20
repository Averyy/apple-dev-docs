# fragmentFunctionName

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The name of the fragment shader function to load from a Metal shader library.

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
var fragmentFunctionName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * fragmentFunctionName;
```

#### Discussion

A program’s fragment shader (sometimes called a *pixel shader*) executes at least once for each pixel in rendered output. The fragment shader takes as input the values output by the vertex shader (after those values have been interpolated by the GPU), and uses them to compute a final color for each pixel.

By default, SceneKit looks for a fragment shader function by this name in the default Metal library. To use shaders from a separate library file, change the [`library`](./library.md) property.

## See Also

### Working With Metal Shaders
- [var vertexFunctionName: String?](./vertexfunctionname.md)
  The name of the vertex shader function to load from a Metal shader library.
- [var library: (any MTLLibrary)?](./library.md)
  The Metal shader library containing shader functions to be used by this program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/fragmentfunctionname)*