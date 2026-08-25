# PresentationPlacement

**Framework**: SwiftUI  
**Kind**: struct

The placement of a presentation within the presenting view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct PresentationPlacement
```

#### Overview

Only sheet presentations respect this placement.

Use values of this type with the [`presentationPlacement(_:)`](view/presentationplacement(_:).md) modifier.

## Topics

### Specifying sheet placement
- [static let automatic: PresentationPlacement](presentationplacement/automatic.md)
  The system determines the placement of the presentation.
- [static let center: PresentationPlacement](presentationplacement/center.md)
  Centers the presentation within the presenting view.
- [static let leading: PresentationPlacement](presentationplacement/leading.md)
  Places the presentation on the leading edge of the presenting view.
- [static let trailing: PresentationPlacement](presentationplacement/trailing.md)
  Places the presentation on the trailing edge of the presenting view.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [struct PresentationContentInteraction](presentationcontentinteraction.md)
  A behavior that you can use to influence how a presentation responds to swipe gestures.
- [func presentationPlacement(PresentationPlacement) -> some View](view/presentationplacement(_:).md)
  Sets the placement of a presentation within the presenting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationplacement)*