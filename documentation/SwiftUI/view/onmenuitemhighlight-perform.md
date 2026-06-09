# onMenuItemHighlight(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the highlight state of a menu item changes.

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
func onMenuItemHighlight(perform action: @escaping (Bool) -> Void) -> some View
```

#### Return Value

A view that triggers `action` when the highlight state changes.

#### Discussion

A state change is triggered as a menu item goes from idle to highlighted and vice versa. Highlighting in this context includes hovering, touching, keyboard navigating, and focusing.

Use this modifier on views inside a menu to observe when the user highlights an item. For example, a photo browser can dim a thumbnail while the user hovers over the `Delete` action:

```swift
@State private var previewingDelete = false
let photo: Photo

PhotoThumbnail(photo: photo)
    .opacity(previewingDelete ? 0.4 : 1)
    .contextMenu {
        Button("Copy") { ... }
        Button("Delete", role: .destructive) {
            ...
        }
        .onMenuItemHighlight { highlighted in
            previewingDelete = highlighted
        }
    }
```

> **Note**: This modifier has no effect when applied outside of a menu context.

## Parameters

- `action`: The action to perform whenever the highlight state of the menu item changes. If the menu item is highlighted, the `action` closure passes `true` as a parameter; otherwise, `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onmenuitemhighlight(perform:))*