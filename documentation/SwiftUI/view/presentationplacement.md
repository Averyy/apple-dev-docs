# presentationPlacement(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the placement of a presentation within the presenting view.

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
nonisolated
func presentationPlacement(_ placement: PresentationPlacement) -> some View
```

#### Discussion

By default, a presentation uses [`automatic`](presentationplacement/automatic.md) placement. Use this modifier to place it on the leading or trailing edge. For example, to maximize the visibility of the primary content behind a presented sheet:

```swift
Map()
    .sheet(isPresented: $isPresented) {
        PlaceDetailView()
            .presentationDetents([.medium, .large])
            .presentationPlacement(.leading)
    }
```

Only sheet presentations respect this placement.

## Parameters

- `placement`: The placement of the presentation within the presenting view.

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
- [struct PresentationPlacement](presentationplacement.md)
  The placement of a presentation within the presenting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationplacement(_:))*