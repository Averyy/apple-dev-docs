# computeFunctionDescriptor

**Framework**: Metal  
**Kind**: property

A descriptor representing the compute pipeline’s function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var computeFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

#### Discussion

You don’t assign instances of [`MTL4FunctionDescriptor`](mtl4functiondescriptor.md) to this property directly, instead assign an instance of one of its subclasses, such as [`MTL4LibraryFunctionDescriptor`](mtl4libraryfunctiondescriptor.md), which represents a function from a Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/computefunctiondescriptor)*