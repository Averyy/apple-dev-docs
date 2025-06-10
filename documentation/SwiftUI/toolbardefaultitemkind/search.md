# search

**Framework**: SwiftUI  
**Kind**: property

The search item added by a `View/searchable(text:isPresented:placement:prompt)` modifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let search: ToolbarDefaultItemKind
```

#### Discussion

Use a `.search` default item kind with `DefaultToolbarItem/init(kind:placment:)` to customize the [`ToolbarItemPlacement`](toolbaritemplacement.md) of a default item kind. The search default item kind can be placed in the `.bottomBar` on iPhone only. All available platforms support `.topBarTrailing` and `.automatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbardefaultitemkind/search)*