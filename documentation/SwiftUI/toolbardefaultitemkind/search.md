# search

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The search item added by a [`searchable(text:isPresented:placement:prompt:)`](../view/searchable%28text,ispresented,placement,prompt%29.md) modifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let search: ToolbarDefaultItemKind
```

## Discussion

Use a `.search` default item kind with [`init(kind:placement:)`](../defaulttoolbaritem/init%28kind,placement%29.md) to customize the [`ToolbarItemPlacement`](../toolbaritemplacement.md) of a default item kind. The search default item kind can be placed in the [`bottomBar`](../toolbaritemplacement/bottombar.md) on all supported platforms. On iOS, it can also be placed in the top bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbardefaultitemkind/search)*