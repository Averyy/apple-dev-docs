# PresentationSizingRoot

**Framework**: SwiftUI  
**Kind**: struct

A proxy to a view provided to the presentation with a defined presentation size.

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
struct PresentationSizingRoot
```

## Topics

### Instance Methods
- [func sizeThatFits(ProposedViewSize) -> CGSize](presentationsizingroot/sizethatfits(_:).md)
  Asks the subview for its size.

## See Also

- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](view/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [struct PresentationAdaptation](presentationadaptation.md)
  Strategies for adapting a presentation to a different size class.
- [func presentationSizing(some PresentationSizing) -> some View](view/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [protocol PresentationSizing](presentationsizing.md)
  A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [struct PresentationSizingContext](presentationsizingcontext.md)
  Contextual information about a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizingroot)*