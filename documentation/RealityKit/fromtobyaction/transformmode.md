# FromToByAction.TransformMode

**Framework**: RealityKit  
**Kind**: enum

Options available to determine the space the bound entity should be relative to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum TransformMode
```

#### Overview

The [`FromToByAction`](fromtobyaction.md) structure accepts this enumeration as an initializer argument when the [`FromToByAction`](fromtobyaction.md) value is a [`Transform`](transform.md) type.

## Topics

### Operators
- [static func == (FromToByAction<Value>.TransformMode, FromToByAction<Value>.TransformMode) -> Bool](fromtobyaction/transformmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FromToByAction.TransformMode.local](fromtobyaction/transformmode/local.md)
  The provided transforms are relative to the transform of the bound entity.
- [FromToByAction.TransformMode.parent](fromtobyaction/transformmode/parent.md)
  The provided transforms are relative to the bound entities parent transform.
- [FromToByAction.TransformMode.relative(to:)](fromtobyaction/transformmode/relative(to:).md)
  The provided transforms are relative to the resolved entities transform.
- [FromToByAction.TransformMode.scene](fromtobyaction/transformmode/scene.md)
  The provided transform is relative to the scene, in world space.
### Initializers
- [init(from: any Decoder) throws](fromtobyaction/transformmode/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](fromtobyaction/transformmode/encode(to:).md)
  Encodes this value into the given encoder.
### Type Properties
- [static var `default`: FromToByAction<Value>.TransformMode](fromtobyaction/transformmode/default.md)
  Default transform mode used by the specializations which use transform mode.
### Default Implementations
- [Equatable Implementations](fromtobyaction/transformmode/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/transformmode)*