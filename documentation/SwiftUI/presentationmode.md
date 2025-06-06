# PresentationMode

**Framework**: SwiftUI  
**Kind**: struct

An indication whether a view is currently presented by another view.

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
struct PresentationMode
```

## Topics

### Checking presentation
- [var isPresented: Bool](presentationmode/ispresented.md)
  Indicates whether a view is currently presented.
### Dismissing presentation
- [func dismiss()](presentationmode/dismiss.md)
  Dismisses the view if it is currently presented.

## See Also

- [var disableAutocorrection: Bool?](environmentvalues/disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var sizeCategory: ContentSizeCategory](environmentvalues/sizecategory.md)
  The size of content.
- [var presentationMode: Binding<PresentationMode>](environmentvalues/presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [var complicationRenderingMode: ComplicationRenderingMode](environmentvalues/complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](environmentvalues/controlactivestate.md)
  The active appearance expected of controls in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationmode)*