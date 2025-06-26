# computeFunctionDescriptor

**Framework**: Metal  
**Kind**: property

A descriptor representing the compute pipeline’s function.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var computeFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

#### Discussion

You don’t assign instances of [`MTL4FunctionDescriptor`](mtl4functiondescriptor.md) to this property directly, instead assign an instance of one of its subclasses, such as [`MTL4LibraryFunctionDescriptor`](mtl4libraryfunctiondescriptor.md), which represents a function from a Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/computefunctiondescriptor)*