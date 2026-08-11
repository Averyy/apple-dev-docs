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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationplacement(_:))*