# sidebar

**Framework**: SwiftUI  
**Kind**: property

The search field appears in the sidebar of a navigation view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var sidebar: SearchFieldPlacement { get }
```

## Mentions

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)

#### Discussion

The precise placement depends on the platform:

- In iOS and iPadOS the search field appears in the section of the navigation bar associated with the sidebar.
- In macOS the search field appears as a sticky header in the sidebar, attached to the toolbar.

If a sidebar isn’t available, like when you apply the searchable modifier to a view other than a navigation split view, SwiftUI uses automatic placement instead.

> **Note**: The search field appears inline with the sidebar’s content when building with Xcode 16 SDKs or earlier.

## See Also

- [static let automatic: SearchFieldPlacement](searchfieldplacement/automatic.md)
  SwiftUI places the search field automatically.
- [static let navigationBarDrawer: SearchFieldPlacement](searchfieldplacement/navigationbardrawer.md)
  The search field appears in the navigation bar.
- [static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement](searchfieldplacement/navigationbardrawer(displaymode:).md)
  The search field appears in the navigation bar using the specified display mode.
- [static let toolbar: SearchFieldPlacement](searchfieldplacement/toolbar.md)
  The search field appears in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement/sidebar)*