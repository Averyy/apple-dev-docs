# PresentationContentInteraction

**Framework**: SwiftUI  
**Kind**: struct

A behavior that you can use to influence how a presentation responds to swipe gestures.

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
struct PresentationContentInteraction
```

#### Overview

Use values of this type with the [`presentationContentInteraction(_:)`](view/presentationcontentinteraction(_:).md) modifier.

## Topics

### Getting interaction behaviors
- [static var automatic: PresentationContentInteraction](presentationcontentinteraction/automatic.md)
  The default swipe behavior for the presentation.
- [static var resizes: PresentationContentInteraction](presentationcontentinteraction/resizes.md)
  A behavior that prioritizes resizing a presentation when swiping, rather than scrolling the content of the presentation.
- [static var scrolls: PresentationContentInteraction](presentationcontentinteraction/scrolls.md)
  A behavior that prioritizes scrolling the content of a presentation when swiping, rather than resizing the presentation.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func presentationDetents(Set<PresentationDetent>) -> some View](view/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](view/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](view/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationDragIndicator(Visibility) -> some View](view/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [struct PresentationDetent](presentationdetent.md)
  A type that represents a height where a sheet naturally rests.
- [protocol CustomPresentationDetent](custompresentationdetent.md)
  The definition of a custom detent with a calculated height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationcontentinteraction)*