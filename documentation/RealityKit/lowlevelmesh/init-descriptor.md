# init(descriptor:)

**Framework**: RealityKit  
**Kind**: init

Constructs a low-level mesh from a descriptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(descriptor: LowLevelMesh.Descriptor) throws
```

#### Discussion

> **Note**: If the descriptor is invalid or if you do not successfully allocate its memory.

## Parameters

- `descriptor`: An object that defines the structure of the low-level mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/init(descriptor:))*