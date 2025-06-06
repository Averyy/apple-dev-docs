# foregroundStyle(_:_:_:)

**Framework**: App Intents  
**Kind**: method

Sets the primary, secondary, and tertiary levels of the foreground style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func foregroundStyle<S1, S2, S3>(_ primary: S1, _ secondary: S2, _ tertiary: S3) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
```

#### Return Value

A view that uses the given foreground styles.

#### Discussion

SwiftUI uses these styles when rendering child views that don’t have an explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `SymbolRenderingMode/palette` rendering mode when you apply this modifier, if you don’t explicitly specify another mode.

## Parameters

- `primary`: The primary color or pattern to use when filling in   the foreground elements. To indicate a specific value, use    or  , or one of the gradient   types, like   . To set a   style that’s relative to the containing view’s style, use one of the   semantic styles, like  .
- `secondary`: The secondary color or pattern to use when   filling in the foreground elements.
- `tertiary`: The tertiary color or pattern to use when   filling in the foreground elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/foregroundstyle(_:_:_:))*