# toolbar

**Framework**: SwiftUI  
**Kind**: property

The search field appears in the toolbar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let toolbar: SearchFieldPlacement
```

#### Discussion

The precise placement depends on the platform:

- In iOS and watchOS, the search field appears below the navigation bar and is revealed by scrolling.
- In iPadOS, the search field appears in the trailing navigation bar.
- In macOS, the search field appears in the trailing toolbar.

## See Also

- [static let automatic: SearchFieldPlacement](searchfieldplacement/automatic.md)
  SwiftUI places the search field automatically.
- [static let navigationBarDrawer: SearchFieldPlacement](searchfieldplacement/navigationbardrawer.md)
  The search field appears in the navigation bar.
- [static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement](searchfieldplacement/navigationbardrawer(displaymode:).md)
  The search field appears in the navigation bar using the specified display mode.
- [static let sidebar: SearchFieldPlacement](searchfieldplacement/sidebar.md)
  The search field appears in the sidebar of a navigation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement/toolbar)*