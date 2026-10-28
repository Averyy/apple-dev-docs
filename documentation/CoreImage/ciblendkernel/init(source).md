# init(source:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a custom blend kernel from a program string.

**Availability**:
- iOS 8.0+ - Deprecated in 12.0
- iPadOS 8.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.14
- tvOS 11.0+ - Deprecated in 12.0
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

A new blend kernel object, or nil if the specified source code does not contain a valid blend kernel routine.

## Discussion

This method is similar to the [`init(source:)`](../cikernel/init%28source%29.md) method of the superclass [`CIKernel`](../cikernel.md), but creates only blend kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [`CIBlendKernel`](../ciblendkernel.md).

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/init(source:))*