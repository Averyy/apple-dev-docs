# MeshDescriptor.Primitives.triangles(_:)

**Framework**: RealityKit  
**Kind**: case

Defines one or more triangles with an integer array of indices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case triangles([UInt32])
```

#### Discussion

Add three vertex index integers per triangle. For example, you can represent a single triangle with three indices.

```swift
.triangles([0, 1, 2])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor/primitives-swift.enum/triangles(_:))*