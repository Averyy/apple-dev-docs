# presentationMode

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A binding to the current presentation mode of the view associated with this environment.

**Availability**:
- iOS 13.0+ - Deprecated in 27.3
- iPadOS 13.0+ - Deprecated in 27.3
- Mac Catalyst 13.0+ - Deprecated in 27.3
- macOS 10.15+ - Deprecated in 27.3
- tvOS 13.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 6.0+ - Deprecated in 27.3

> **Deprecated**: Use [`isPresented`](./ispresented.md) or [`dismiss`](./dismiss.md) instead.

## Declaration

```swift
var presentationMode: Binding<PresentationMode> { get }
```

## See Also

### Deprecated properties
- [var accessibilityShowButtonShapes: Bool](./accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var complicationRenderingMode: ComplicationRenderingMode](./complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](./controlactivestate.md)
  The active appearance expected of controls in a window.
- [var disableAutocorrection: Bool?](./disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [struct PresentationMode](../presentationmode.md)
  An indication whether a view is currently presented by another view.
- [var sizeCategory: ContentSizeCategory](./sizecategory.md)
  The size of content.
- [var imagePlaygroundPersonalizationPolicy: ImagePlaygroundPersonalizationPolicy](./imageplaygroundpersonalizationpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/presentationmode)*