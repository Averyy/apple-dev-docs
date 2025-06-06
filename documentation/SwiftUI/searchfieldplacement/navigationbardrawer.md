# navigationBarDrawer

**Framework**: SwiftUI  
**Kind**: property

The search field appears in the navigation bar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let navigationBarDrawer: SearchFieldPlacement
```

#### Discussion

The field appears below any navigation bar title and uses the [`automatic`](searchfieldplacement/navigationbardrawerdisplaymode/automatic.md) display mode to configure when to hide the search field. To choose a different display mode, use [`navigationBarDrawer(displayMode:)`](searchfieldplacement/navigationbardrawer(displaymode:).md) instead.

## See Also

- [static let automatic: SearchFieldPlacement](searchfieldplacement/automatic.md)
  SwiftUI places the search field automatically.
- [static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement](searchfieldplacement/navigationbardrawer(displaymode:).md)
  The search field appears in the navigation bar using the specified display mode.
- [static let sidebar: SearchFieldPlacement](searchfieldplacement/sidebar.md)
  The search field appears in the sidebar of a navigation view.
- [static let toolbar: SearchFieldPlacement](searchfieldplacement/toolbar.md)
  The search field appears in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement/navigationbardrawer)*