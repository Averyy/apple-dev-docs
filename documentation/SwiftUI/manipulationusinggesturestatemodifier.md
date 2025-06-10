# ManipulationUsingGestureStateModifier

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
struct ManipulationUsingGestureStateModifier
```

## Relationships

### Conforms To
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
- [struct ManipulableResponderModifier](manipulablerespondermodifier.md)
- [struct ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [struct ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [struct ManipulationGestureModifier](manipulationgesturemodifier.md)
- [enum Manipulable](manipulable.md)
  A namespace for various manipulable related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulationusinggesturestatemodifier)*