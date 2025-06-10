# modifier(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies a modifier to a view and returns a new view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>
```

## Mentions

- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)

#### Discussion

Use this modifier to combine a [`View`](view.md) and a [`ViewModifier`](viewmodifier.md), to create a new view. For example, if you create a view modifier for a new kind of caption with blue text surrounded by a rounded rectangle:

```swift
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

You can use [`modifier(_:)`](view/modifier(_:).md) to extend [`View`](view.md) to create new modifier for applying the `BorderedCaption` defined above:

```swift
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

Then you can apply the bordered caption to any view:

```swift
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

![A screenshot showing the image of a bus with a caption reading](https://docs-assets.developer.apple.com/published/dc0170d83bbfb353e45ad5d2e90f7fe6/SwiftUI-View-ViewModifier%402x.png)

## Parameters

- `modifier`: The modifier to apply to this view.

## See Also

- [Configuring views](configuring-views.md)
  Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
  Bundle view modifiers that you regularly reuse into a custom view modifier.
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
- [struct ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [enum Manipulable](manipulable.md)
  A namespace for various manipulable related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/modifier(_:))*