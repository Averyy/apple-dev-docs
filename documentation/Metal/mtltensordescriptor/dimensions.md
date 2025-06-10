# dimensions

**Framework**: Metal  
**Kind**: property

An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.

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
var dimensions: MTLTensorExtents { get set }
```

#### Discussion

The default value of this property is a rank one extents with size one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/dimensions)*