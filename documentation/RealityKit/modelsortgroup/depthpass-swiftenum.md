# ModelSortGroup.DepthPass

**Framework**: RealityKit  
**Kind**: enum

Options that indicate when the renderer draws a model’s depth relative to its color.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum DepthPass
```

## Topics

### Operators
- [static func == (ModelSortGroup.DepthPass, ModelSortGroup.DepthPass) -> Bool](modelsortgroup/depthpass-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ModelSortGroup.DepthPass.postPass](modelsortgroup/depthpass-swift.enum/postpass.md)
  An option that instructs the renderer to draw the depth of a model only after it draws the colors for all the models in the group first.
- [ModelSortGroup.DepthPass.prePass](modelsortgroup/depthpass-swift.enum/prepass.md)
  An option that instructs the renderer to draw the depth of all the models in the group before it draws any model’s color.
### Instance Properties
- [var hashValue: Int](modelsortgroup/depthpass-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](modelsortgroup/depthpass-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](modelsortgroup/depthpass-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroup/depthpass-swift.enum)*