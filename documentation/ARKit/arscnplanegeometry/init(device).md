# init(device:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a SceneKit plane geometry for rendering with the specified Metal device object.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
convenience init?(device: any MTLDevice)
```

```objc
+ (instancetype) planeGeometryWithDevice:(id<MTLDevice>) device;
```

#### Return Value

A new SceneKit plane geometry, or `nil` if the Metal device is unavailable.

#### Discussion

A newly created [`ARSCNPlaneGeometry`](../arscnplanegeometry.md) instance does not represent any specific plane; use the [`update(from:)`](./update%28from%29.md) method to make the geometry match the estimated shape of a specific plane anchor.

The geometry contains a single geometry element; as such, assigning more than one material has no visible effect (see the inherited [`materials`](../../SceneKit/scngeometry/materials.md) property).

## Parameters

- `device`: The Metal device to use for rendering the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry/init(device:))*