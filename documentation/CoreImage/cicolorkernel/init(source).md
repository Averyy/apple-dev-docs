# init(source:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a color kernel object from the specified kernel source code.

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

#### Return Value

A new color kernel object, or `nil` if the specified source code does not contain a valid color kernel routine.

#### Discussion

This method is similar to the [`init(source:)`](../cikernel/init%28source%29.md) method of the superclass [`CIKernel`](../cikernel.md), but creates only color kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [`CIColorKernel`](../cicolorkernel.md).

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorkernel/init(source:))*