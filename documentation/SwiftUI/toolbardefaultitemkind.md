# ToolbarDefaultItemKind

**Framework**: SwiftUI  
**Kind**: struct

A kind of toolbar item a `View` adds by default.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ToolbarDefaultItemKind
```

#### Overview

`View`s can add toolbar items clients may wish to remove or customize. A default item kind can be passed to the [`toolbar(removing:)`](view/toolbar(removing:).md) modifier to remove the item. Documentation on the `View` placing the default item should reference the `ToolbarDefaultItemKind` used to remove the item.

## Topics

### Getting the default item types
- [static let sidebarToggle: ToolbarDefaultItemKind](toolbardefaultitemkind/sidebartoggle.md)
  The sidebar toggle toolbar item a `NavigationSplitView` adds by default.
### Type Properties
- [static let search: ToolbarDefaultItemKind](toolbardefaultitemkind/search.md)
  The search item added by a `View/searchable(text:isPresented:placement:prompt)` modifier.
- [static let title: ToolbarDefaultItemKind](toolbardefaultitemkind/title.md)
  The title and subtitle shown in title bar / navigation bar.

## See Also

- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](view/toolbar(removing:).md)
  Remove a toolbar item present by default


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbardefaultitemkind)*