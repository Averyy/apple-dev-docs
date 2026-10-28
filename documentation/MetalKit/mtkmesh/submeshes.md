# submeshes

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

An array of submeshes containing index buffers referencing the mesh vertices.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var submeshes: [MTKSubmesh] { get }
```

```objc
@property (nonatomic, readonly, nonnull) NSArray<MTKSubmesh *> * submeshes;
```

## Discussion

Submeshes may also contain texture materials to apply when rendering the mesh object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh/submeshes)*