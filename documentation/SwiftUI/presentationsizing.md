# PresentationSizing

**Framework**: SwiftUI  
**Kind**: protocol

A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol PresentationSizing
```

#### Overview

You don’t need to define your own version of this protocol. The system implementations of [`form`](presentationsizing/form.md), [`page`](presentationsizing/page.md), and [`fitted`](presentationsizing/fitted.md) are conveniences that automatically adapt to different device and screen sizes. If you do want to define your own sizing, first consider using the modifiers `PresenationSizing/sticky(horizontal:vertical:)` and [`fitted(horizontal:vertical:)`](presentationsizing/fitted(horizontal:vertical:).md). For example, to define your own sizing that proposes a 400x400 square size:

```swift
protocol SquareSizing: PresentationSizing {
    func proposedSize(
        for subview: PresentationSizingRoot,
        context: PresentationSizingContext
    ) {
        .init(width: 400, height: 400)
    }
}

extension PresentationSizing where Self == SquareSizing {
    public static var square: Self { SquareSizing() }
}
```

Then, at the callsite, you can modify `.square` just like system sizings, for example, to fit its content vertically:

```swift
.presentationSizing(.square.fitted(horizontal: false, vertical: true))
```

> **Note**: [`presentationSizing(_:)`](view/presentationsizing(_:).md)

[`presentationSizing(_:)`](view/presentationsizing(_:).md)

## Topics

### Getting built-in presentation size
- [static var automatic: AutomaticPresentationSizing](presentationsizing/automatic.md)
  The default presentation sizing, appropriate for the platform.
- [static var fitted: FittedPresentationSizing](presentationsizing/fitted.md)
  The presentation sizing is dictated by the ideal size of the content
- [static var form: FormPresentationSizing](presentationsizing/form.md)
  The size is appropriate for forms and slightly less wide than`.page`
- [static var page: PagePresentationSizing](presentationsizing/page.md)
  The size is roughly the size of a page of paper, appropriate for informational or compositional content.
### Creating custom presentation size
- [func fitted(horizontal: Bool, vertical: Bool) -> some PresentationSizing](presentationsizing/fitted(horizontal:vertical:).md)
- [func proposedSize(for: PresentationSizingRoot, context: PresentationSizingContext) -> ProposedViewSize](presentationsizing/proposedsize(for:context:).md)
- [func sticky(horizontal: Bool, vertical: Bool) -> some PresentationSizing](presentationsizing/sticky(horizontal:vertical:).md)
  Modifies self to be sticky in the specified dimensions — growing, but not shrinking.
### Supporting types
- [struct AutomaticPresentationSizing](automaticpresentationsizing.md)
  The default presentation sizing, appropriate for the platform.
- [struct FittedPresentationSizing](fittedpresentationsizing.md)
  The size of the presentation is dictated by the ideal size of the content.
- [struct FormPresentationSizing](formpresentationsizing.md)
  The size is appropriate for forms and slightly less wide than`.page`
- [struct PagePresentationSizing](pagepresentationsizing.md)
  The size is roughly the size of a page of paper, appropriate for informational or compositional content.

## Relationships

### Conforming Types
- [AutomaticPresentationSizing](automaticpresentationsizing.md)
- [FittedPresentationSizing](fittedpresentationsizing.md)
- [FormPresentationSizing](formpresentationsizing.md)
- [PagePresentationSizing](pagepresentationsizing.md)

## See Also

- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](view/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [struct PresentationAdaptation](presentationadaptation.md)
  Strategies for adapting a presentation to a different size class.
- [func presentationSizing(some PresentationSizing) -> some View](view/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [struct PresentationSizingRoot](presentationsizingroot.md)
  A proxy to a view provided to the presentation with a defined presentation size.
- [struct PresentationSizingContext](presentationsizingcontext.md)
  Contextual information about a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizing)*