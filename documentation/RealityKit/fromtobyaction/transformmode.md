# FromToByAction.TransformMode

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Options available to determine the space the bound entity should be relative to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum TransformMode
```

## Overview

The [`FromToByAction`](../fromtobyaction.md) structure accepts this enumeration as an initializer argument when the [`FromToByAction`](../fromtobyaction.md) value is a [`Transform`](../transform.md) type.

## Topics

### Enumeration Cases
- [FromToByAction.TransformMode.local](./transformmode/local.md)
  The provided transforms are relative to the transform of the bound entity.
- [FromToByAction.TransformMode.parent](./transformmode/parent.md)
  The provided transforms are relative to the bound entities parent transform.
- [FromToByAction.TransformMode.relative(to:)](./transformmode/relative%28to%29.md)
  The provided transforms are relative to the resolved entities transform.
- [FromToByAction.TransformMode.scene](./transformmode/scene.md)
  The provided transform is relative to the scene, in world space.
### Type Properties
- [static var `default`: FromToByAction<Value>.TransformMode](./transformmode/default.md)
  Default transform mode used by the specializations which use transform mode.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/transformmode)*