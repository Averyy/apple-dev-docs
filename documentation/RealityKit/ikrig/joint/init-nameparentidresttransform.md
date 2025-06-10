# init(name:parentID:restTransform:)

**Framework**: RealityKit  
**Kind**: init

Creates a joint with the provided base elements.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(name: String, parentID: IKRig.Joint.ID? = nil, restTransform: Transform = .identity)
```

## Parameters

- `name`: The name of the new joint.
- `parentID`: The name of the parent joint if there is one.
- `restTransform`: The offset of this joint from its parent (local space).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/joint/init(name:parentid:resttransform:))*