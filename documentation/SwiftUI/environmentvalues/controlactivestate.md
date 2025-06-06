# controlActiveState

**Framework**: SwiftUI  
**Kind**: property

The active appearance expected of controls in a window.

**Availability**:
- macOS 10.15+

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

- [var disableAutocorrection: Bool?](environmentvalues/disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var sizeCategory: ContentSizeCategory](environmentvalues/sizecategory.md)
  The size of content.
- [var presentationMode: Binding<PresentationMode>](environmentvalues/presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [struct PresentationMode](presentationmode.md)
  An indication whether a view is currently presented by another view.
- [var complicationRenderingMode: ComplicationRenderingMode](environmentvalues/complicationrenderingmode.md)
  The complication rendering mode for the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/controlactivestate)*