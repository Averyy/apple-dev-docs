# controlActiveState

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The active appearance expected of controls in a window.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use `EnvironmentValues.appearsActive` instead.

## Declaration

```swift
var controlActiveState: ControlActiveState { get set }
```

#### Discussion

`ControlActiveState` and `EnvironmentValues.controlActiveState` are deprecated, use `EnvironmentValues.appearsActive` instead.

Starting with macOS 15.0, the value of this environment property is strictly mapped to and from `EnvironmentValues.appearsActive` as follows:

- `appearsActive == true`, `controlActiveState` returns `.key`
- `appearsActive == false`, `controlActiveState` returns `.inactive`
- `controlActiveState` is set to `.key` or `.active`, `appearsActive` will be set to `true`.
- `controlActiveState` is set to `.inactive`, `appearsActive` will be set to `false`.

## See Also

### Deprecated properties
- [var accessibilityShowButtonShapes: Bool](./accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var complicationRenderingMode: ComplicationRenderingMode](./complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var disableAutocorrection: Bool?](./disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var presentationMode: Binding<PresentationMode>](./presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [var sizeCategory: ContentSizeCategory](./sizecategory.md)
  The size of content.
- [var imagePlaygroundPersonalizationPolicy: ImagePlaygroundPersonalizationPolicy](./imageplaygroundpersonalizationpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/controlactivestate)*