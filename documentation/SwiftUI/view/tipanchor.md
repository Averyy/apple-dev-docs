# tipAnchor(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func tipAnchor<AnchorID>(_ id: AnchorID) -> some View where AnchorID : Hashable, AnchorID : Sendable
```

#### Return Value

A new version of the view that writes to the key.

#### Discussion

Use this modifier to specify an anchor view for a `TipView`’s arrow to point towards.

```swift
struct TrailRow: View {
    let trail: Trail

    var body: some View {
        HStack {
            Text(trail.name)

            Button(action: trail.favorite) {
                Image(systemName: "star")
            }
            .tipAnchor("FavoriteTrailTipAnchor")
        }

        TipView(FavoriteTrailTip(), anchorID: "FavoriteTrailTipAnchor")
    }
}
```

## Parameters

- `id`: The anchored view’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipanchor(_:))*