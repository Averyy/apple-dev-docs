# init(source:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a single kernel object.

**Availability**:
- iOS 8.0+ - Deprecated in 12.0
- iPadOS 8.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.14
- tvOS - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
convenience init?(source string: String)
```

```objc
+ (instancetype) kernelWithString:(NSString *) string;
```

## Return Value

A new kernel object. The class of the returned object can be [`CIKernel`](../cikernel.md), [`CIColorKernel`](../cicolorkernel.md), or [`CIWarpKernel`](../ciwarpkernel.md) depending on the type of routine specified in the Core Image Kernel Language source code string.

## Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.

## See Also

### Related Documentation
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397)
### Deprecated
- [class func makeKernels(source: String) -> [CIKernel]?](./makekernels%28source%29.md)
  Creates and returns and array of  `CIKernel` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/init(source:))*