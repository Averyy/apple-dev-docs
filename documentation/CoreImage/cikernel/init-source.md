# init(source:)

**Framework**: Core Image  
**Kind**: init

Creates a single kernel object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init?(source string: String)
```

#### Return Value

A new kernel object. The class of the returned object can be [`CIKernel`](cikernel.md), [`CIColorKernel`](cicolorkernel.md), or [`CIWarpKernel`](ciwarpkernel.md) depending on the type of routine specified in the Core Image Kernel Language source code string.

#### Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the   keyword.

## See Also

- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Core Image Kernel Language Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397)
- [class func makeKernels(source: String) -> [CIKernel]?](cikernel/makekernels(source:).md)
  Creates and returns and array of  `CIKernel` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/init(source:))*