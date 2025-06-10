# webViewContextMenu(menu:)

**Framework**: SwiftUI  
**Kind**: method

Adds an item-based context menu to a WebView, replacing the default set of context menu items.

**Availability**:
- macOS 15.4+

## Declaration

```swift
nonisolated
func webViewContextMenu(@ViewBuilder menu: @escaping @MainActor (WebView.ActivatedElementInfo) -> some View) -> some View
```

#### Return Value

A view that can display an item-based context menu.

## Parameters

- `menu`: A closure that produces the menu. The single parameter to the closure describes the type of webpage element that was acted upon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewcontextmenu(menu:))*