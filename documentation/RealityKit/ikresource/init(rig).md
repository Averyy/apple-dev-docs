# init(rig:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new resource instance for a single solver using the given rig and an automatic solver identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(rig: IKRig) throws
```

## Discussion

> **Throws**: Validation errors for the given rig structure.

## Parameters

- `rig`: The inverse kinematics rig to be serialised into the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikresource/init(rig:))*