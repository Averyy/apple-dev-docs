# dimensions

**Framework**: Metal  
**Kind**: property

An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.

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
var dimensions: MTLTensorExtents { get set }
```

#### Discussion

The default value of this property is a rank one extents with size one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/dimensions)*