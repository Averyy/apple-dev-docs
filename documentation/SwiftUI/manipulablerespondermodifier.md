# ManipulableResponderModifier

**Framework**: SwiftUI  
**Kind**: struct

A view modifier that makes a view respond to manipulation hand gestures.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
struct ManipulableResponderModifier
```

#### Overview

SwiftUI applies this type on your behalf as part of the `manipulable` modifiers. You don’t create it directly.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [ViewModifier](viewmodifier.md)

## See Also

- [Configuring views](configuring-views.md)
  Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
  Bundle view modifiers that you regularly reuse into a custom view modifier.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](view/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [protocol ViewModifier](viewmodifier.md)
  A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [struct EmptyModifier](emptymodifier.md)
  An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [struct ModifiedContent](modifiedcontent.md)
  A value with a modifier applied to it.
- [protocol EnvironmentalModifier](environmentalmodifier.md)
  A modifier that must resolve to a concrete modifier in an environment before use.
- [struct ManipulableModifier](manipulablemodifier.md)
  A view modifier that lets hand gestures move, rotate, and scale a view.
- [struct ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
  A view modifier that applies a 3D affine transform to a view and lets hand gestures change it.
- [struct ManipulationGeometryModifier](manipulationgeometrymodifier.md)
  A view modifier that tracks the geometry a manipulation gesture acts on.
- [struct ManipulationGestureModifier](manipulationgesturemodifier.md)
  A view modifier that recognizes manipulation hand gestures and reports their state through a binding.
- [struct ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
  A view modifier that applies the manipulation state from a gesture on another view.
- [enum Manipulable](manipulable.md)
  A namespace for various manipulable related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulablerespondermodifier)*