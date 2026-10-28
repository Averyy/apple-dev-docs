# vertexDescriptor

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The organization of vertex data in an attribute’s argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var vertexDescriptor: MTLVertexDescriptor? { get set }
```

```objc
@property (nonatomic, copy, nullable) MTLVertexDescriptor * vertexDescriptor;
```

## Discussion

An [`MTLVertexDescriptor`](../mtlvertexdescriptor.md) instance is used to describe the organization of per-vertex input structs passed in an argument of a vertex shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexdescriptor)*