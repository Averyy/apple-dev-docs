# library

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The Metal shader library containing shader functions to be used by this program.

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
var library: (any MTLLibrary)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLLibrary> library;
```

#### Discussion

If this property’s value is nil (the default), SceneKit loads shader functions from the default Metal library. Change this value if you have compiled a separate `.metallib` file for the shader functions you wish to use.

## See Also

### Related Documentation
- [func makeDefaultLibrary() -> (any MTLLibrary)?](../../Metal/mtldevice/makedefaultlibrary%28%29.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
### Working With Metal Shaders
- [var vertexFunctionName: String?](./vertexfunctionname.md)
  The name of the vertex shader function to load from a Metal shader library.
- [var fragmentFunctionName: String?](./fragmentfunctionname.md)
  The name of the fragment shader function to load from a Metal shader library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/library)*