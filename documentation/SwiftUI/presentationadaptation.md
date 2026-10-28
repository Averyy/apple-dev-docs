# PresentationAdaptation

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Strategies for adapting a presentation to a different size class.

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
struct PresentationAdaptation
```

## Overview

Use values of this type with the [`presentationCompactAdaptation(_:)`](./view/presentationcompactadaptation%28_%29.md) and [`presentationCompactAdaptation(horizontal:vertical:)`](./view/presentationcompactadaptation%28horizontal,vertical%29.md) modifiers.

## Topics

### Getting adaptation strategies
- [static var automatic: PresentationAdaptation](./presentationadaptation/automatic.md)
  Use the default presentation adaptation.
- [static var none: PresentationAdaptation](./presentationadaptation/none.md)
  Don’t adapt for the size class, if possible.
- [static var fullScreenCover: PresentationAdaptation](./presentationadaptation/fullscreencover.md)
  Prefer a full-screen-cover appearance when adapting for size classes.
- [static var popover: PresentationAdaptation](./presentationadaptation/popover.md)
  Prefer a popover appearance when adapting for size classes.
- [static var sheet: PresentationAdaptation](./presentationadaptation/sheet.md)
  Prefer a sheet appearance when adapting for size classes.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adapting a presentation size
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28horizontal,vertical%29.md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28_%29.md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationSizing(some PresentationSizing) -> some View](./view/presentationsizing%28_%29.md)
  Sets the sizing of the containing presentation.
- [protocol PresentationSizing](./presentationsizing.md)
  A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [struct PresentationSizingRoot](./presentationsizingroot.md)
  A proxy to a view provided to the presentation with a defined presentation size.
- [struct PresentationSizingContext](./presentationsizingcontext.md)
  Contextual information about a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationadaptation)*