# init(source:)

**Framework**: Core Image  
**Kind**: init

Creates a custom blend kernel from a program string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(source string: String)
```

#### Return Value

A new blend kernel object, or nil if the specified source code does not contain a valid blend kernel routine.

#### Discussion

This method is similar to the [`init(source:)`](cikernel/init(source:).md) method of the superclass [`CIKernel`](cikernel.md), but creates only blend kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [`CIBlendKernel`](ciblendkernel.md).

## Parameters

- `string`: A program in the Core Image Kernel Language that contains a single routine marked using the   keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/init(source:))*