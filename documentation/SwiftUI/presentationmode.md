# PresentationMode

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An indication whether a view is currently presented by another view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.3
- iPadOS 13.0+ - Deprecated in 27.3
- Mac Catalyst 13.0+ - Deprecated in 27.3
- macOS 10.15+ - Deprecated in 27.3
- tvOS 13.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 6.0+ - Deprecated in 27.3

> **Deprecated**: Use [`isPresented`](./environmentvalues/ispresented.md) or [`dismiss`](./environmentvalues/dismiss.md) instead.

## Declaration

```swift
struct PresentationMode
```

## Topics

### Checking presentation
- [var isPresented: Bool](./presentationmode/ispresented.md)
  Indicates whether a view is currently presented.
### Dismissing presentation
- [func dismiss()](./presentationmode/dismiss%28%29.md)
  Dismisses the view if it is currently presented.

## See Also

### Deprecated properties
- [var accessibilityShowButtonShapes: Bool](./environmentvalues/accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var complicationRenderingMode: ComplicationRenderingMode](./environmentvalues/complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](./environmentvalues/controlactivestate.md)
  The active appearance expected of controls in a window.
- [var disableAutocorrection: Bool?](./environmentvalues/disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var presentationMode: Binding<PresentationMode>](./environmentvalues/presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [var sizeCategory: ContentSizeCategory](./environmentvalues/sizecategory.md)
  The size of content.
- [var imagePlaygroundPersonalizationPolicy: ImagePlaygroundPersonalizationPolicy](./environmentvalues/imageplaygroundpersonalizationpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationmode)*