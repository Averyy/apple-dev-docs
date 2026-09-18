# Manipulable

**Framework**: SwiftUI  
**Kind**: enum

A namespace for various manipulable related types.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum Manipulable
```

## Topics

### Structures
- [Manipulable.Event](manipulable/event.md)
  Describes an event generated during a manipulation gesture.
- [Manipulable.GestureState](manipulable/gesturestate.md)
  Describes the state of a manipulation gesture.
- [Manipulable.Inertia](manipulable/inertia.md)
  Describes inertia of a view that defines how much a view resists being manipulated.
- [Manipulable.InputDevice](manipulable/inputdevice.md)
  Describes an input device like a hand or a trackpad.
- [Manipulable.Operation](manipulable/operation.md)
  Describes an operation applied to a view when a person is manipulating a view.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [struct ManipulableResponderModifier](manipulablerespondermodifier.md)
  A view modifier that makes a view respond to manipulation hand gestures.
- [struct ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
  A view modifier that applies a 3D affine transform to a view and lets hand gestures change it.
- [struct ManipulationGeometryModifier](manipulationgeometrymodifier.md)
  A view modifier that tracks the geometry a manipulation gesture acts on.
- [struct ManipulationGestureModifier](manipulationgesturemodifier.md)
  A view modifier that recognizes manipulation hand gestures and reports their state through a binding.
- [struct ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
  A view modifier that applies the manipulation state from a gesture on another view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable)*