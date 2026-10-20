# makeKernels(source:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns and array of  `CIKernel` objects.

**Availability**:
- iOS 8.0+ - Deprecated in 12.0
- iPadOS 8.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.14
- tvOS - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
class func makeKernels(source string: String) -> [CIKernel]?
```

```objc
+ (NSArray<CIKernel *> *) kernelsWithString:(NSString *) string;
```

#### Return Value

An array of  `CIKernel` objects. The array contains one `CIKernel` objects for each kernel routine in the supplied string. Each object in the array can be of class [`CIKernel`](../cikernel.md), [`CIColorKernel`](../cicolorkernel.md), or [`CIWarpKernel`](../ciwarpkernel.md) depending on the corresponding routine specified in the Core Image Kernel Language source code string.

#### Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Parameters

- `string`: A program in the Core Image Kernel Language that contains one or more routines, each of which is marked using the `kernel` keyword.

## See Also

### Deprecated
- [convenience init?(source: String)](./init%28source%29.md)
  Creates a single kernel object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/makekernels(source:))*