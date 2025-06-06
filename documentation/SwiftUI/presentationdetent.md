# PresentationDetent

**Framework**: SwiftUI  
**Kind**: struct

A type that represents a height where a sheet naturally rests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct PresentationDetent
```

## Topics

### Getting built-in detents
- [static let large: PresentationDetent](presentationdetent/large.md)
  The system detent for a sheet at full height.
- [static let medium: PresentationDetent](presentationdetent/medium.md)
  The system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.
### Creating custom detents
- [static func custom<D>(D.Type) -> PresentationDetent](presentationdetent/custom(_:).md)
  A custom detent with a calculated height.
- [static func fraction(CGFloat) -> PresentationDetent](presentationdetent/fraction(_:).md)
  A custom detent with the specified fractional height.
- [static func height(CGFloat) -> PresentationDetent](presentationdetent/height(_:).md)
  A custom detent with the specified height.
- [PresentationDetent.Context](presentationdetent/context.md)
  Information that you use to calculate the presentation’s height.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func presentationDetents(Set<PresentationDetent>) -> some View](view/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](view/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](view/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationDragIndicator(Visibility) -> some View](view/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [protocol CustomPresentationDetent](custompresentationdetent.md)
  The definition of a custom detent with a calculated height.
- [struct PresentationContentInteraction](presentationcontentinteraction.md)
  A behavior that you can use to influence how a presentation responds to swipe gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationdetent)*