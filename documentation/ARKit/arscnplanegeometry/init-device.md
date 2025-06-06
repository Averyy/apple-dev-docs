# init(device:)

**Framework**: ARKit  
**Kind**: init

Creates a SceneKit plane geometry for rendering with the specified Metal device object.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
convenience init?(device: any MTLDevice)
```

#### Return Value

A new SceneKit plane geometry, or `nil` if the Metal device is unavailable.

#### Discussion

A newly created [`ARSCNPlaneGeometry`](arscnplanegeometry.md) instance does not represent any specific plane; use the [`update(from:)`](arscnplanegeometry/update(from:).md) method to make the geometry match the estimated shape of a specific plane anchor.

The geometry contains a single geometry element; as such, assigning more than one material has no visible effect (see the inherited [`materials`](https://developer.apple.com/documentation/scenekit/scngeometry/1523472-materials) property).

## Parameters

- `device`: The Metal device to use for rendering the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry/init(device:))*