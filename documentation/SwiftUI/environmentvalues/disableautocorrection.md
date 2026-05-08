# disableAutocorrection

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that determines whether the view hierarchy has auto-correction enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var disableAutocorrection: Bool? { get set }
```

#### Discussion

When the value is `nil`, SwiftUI uses the system default. The default value is `nil`.

## See Also

- [var sizeCategory: ContentSizeCategory](environmentvalues/sizecategory.md)
  The size of content.
- [var presentationMode: Binding<PresentationMode>](environmentvalues/presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [struct PresentationMode](presentationmode.md)
  An indication whether a view is currently presented by another view.
- [var complicationRenderingMode: ComplicationRenderingMode](environmentvalues/complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](environmentvalues/controlactivestate.md)
  The active appearance expected of controls in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/disableautocorrection)*