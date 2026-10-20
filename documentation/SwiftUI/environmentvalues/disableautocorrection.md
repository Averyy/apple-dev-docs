# disableAutocorrection

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view hierarchy has auto-correction enabled.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- macOS 10.15+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- tvOS 13.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)
- watchOS 8.0+ - Deprecated in 27.2 (renamed: autocorrectionDisabled)

## Declaration

```swift
var disableAutocorrection: Bool? { get set }
```

#### Discussion

When the value is `nil`, SwiftUI uses the system default. The default value is `nil`.

## See Also

### Deprecated properties
- [var accessibilityShowButtonShapes: Bool](./accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var complicationRenderingMode: ComplicationRenderingMode](./complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](./controlactivestate.md)
  The active appearance expected of controls in a window.
- [var presentationMode: Binding<PresentationMode>](./presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [var sizeCategory: ContentSizeCategory](./sizecategory.md)
  The size of content.
- [var imagePlaygroundPersonalizationPolicy: ImagePlaygroundPersonalizationPolicy](./imageplaygroundpersonalizationpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/disableautocorrection)*