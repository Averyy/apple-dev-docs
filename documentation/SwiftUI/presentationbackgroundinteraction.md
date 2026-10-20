# PresentationBackgroundInteraction

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The kinds of interaction available to views behind a presentation.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
struct PresentationBackgroundInteraction
```

#### Overview

Use values of this type with the [`presentationBackgroundInteraction(_:)`](./view/presentationbackgroundinteraction%28_%29.md) modifier.

## Topics

### Getting interaction types
- [static var automatic: PresentationBackgroundInteraction](./presentationbackgroundinteraction/automatic.md)
  The default background interaction for the presentation.
- [static var disabled: PresentationBackgroundInteraction](./presentationbackgroundinteraction/disabled.md)
  People can’t interact with the view behind a presentation.
- [static var enabled: PresentationBackgroundInteraction](./presentationbackgroundinteraction/enabled.md)
  People can interact with the view behind a presentation.
- [static func enabled(upThrough: PresentationDetent) -> PresentationBackgroundInteraction](./presentationbackgroundinteraction/enabled%28upthrough%29.md)
  People can interact with the view behind a presentation up through a specified detent.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Styling a sheet and its background
- [func presentationCornerRadius(CGFloat?) -> some View](./view/presentationcornerradius%28_%29.md)
  Requests that the presentation have a specific corner radius.
- [func presentationBackground<S>(S) -> some View](./view/presentationbackground%28_%29.md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](./view/presentationbackground%28alignment,content%29.md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./view/presentationbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationbackgroundinteraction)*