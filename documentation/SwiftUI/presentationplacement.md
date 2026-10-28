# PresentationPlacement

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The placement of a presentation within the presenting view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct PresentationPlacement
```

## Overview

Only sheet presentations respect this placement.

Use values of this type with the [`presentationPlacement(_:)`](./view/presentationplacement%28_%29.md) modifier.

## Topics

### Specifying sheet placement
- [static let automatic: PresentationPlacement](./presentationplacement/automatic.md)
  The system determines the placement of the presentation.
- [static let center: PresentationPlacement](./presentationplacement/center.md)
  Centers the presentation within the presenting view.
- [static let leading: PresentationPlacement](./presentationplacement/leading.md)
  Places the presentation on the leading edge of the presenting view.
- [static let trailing: PresentationPlacement](./presentationplacement/trailing.md)
  Places the presentation on the trailing edge of the presenting view.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a sheet’s height and placement
- [func presentationDetents(Set<PresentationDetent>) -> some View](./view/presentationdetents%28_%29.md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](./view/presentationdetents%28_,selection%29.md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](./view/presentationcontentinteraction%28_%29.md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationDragIndicator(Visibility) -> some View](./view/presentationdragindicator%28_%29.md)
  Sets the visibility of the drag indicator on top of a sheet.
- [struct PresentationDetent](./presentationdetent.md)
  A type that represents a height where a sheet naturally rests.
- [protocol CustomPresentationDetent](./custompresentationdetent.md)
  The definition of a custom detent with a calculated height.
- [struct PresentationContentInteraction](./presentationcontentinteraction.md)
  A behavior that you can use to influence how a presentation responds to swipe gestures.
- [func presentationPlacement(PresentationPlacement) -> some View](./view/presentationplacement%28_%29.md)
  Sets the placement of a presentation within the presenting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationplacement)*