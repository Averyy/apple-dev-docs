# popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)

**Framework**: SwiftUI  
**Kind**: method

Presents a popover tip on the modified view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@preconcurrency
nonisolated func popoverTip(_ tip: (any Tip)?, isPresented: Binding<Bool>? = nil, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, action: @escaping @MainActor (Tips.Action) -> Void = { _ in }) -> some View
```

##### Discussion

Use this modifier to present a tip as a popover on an existing view when the tip becomes eligible for display.

```swift
struct TrailRow: View {
    let trail: Trail

    var body: some View {
        VStack {
            HStack {
                Text(trail.name)

                Button(action: trail.favorite) {
                    Image(systemName: "star")
                }
            }
        }
        .popoverTip(FavoriteTrailTip(), attachmentAnchor: .point(.center), arrowEdge: .top)
    }
}
```

## Parameters

- `tip`: The tip to display.
- `isPresented`: A binding that will automatically update to true when a tip is displayed. This value can be changed to temporarily hide or show a currently displayable tip. If this value is  , the popover will automatically be dismissed based on the tip’s status and display rules.
- `attachmentAnchor`: The positioning anchor that defines the attachment point of the popover. The default is bounds.
- `arrowEdge`: The edge of the attachmentAnchor that defines the location of the popover’s arrow. By default, the system will choose the best orientation of the popover’s arrow.
- `action`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:))*