# navigationBarDrawer(displayMode:)

**Framework**: SwiftUI  
**Kind**: method

The search field appears in the navigation bar using the specified display mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement
```

#### Discussion

The field appears below any navigation bar title. The system can hide the field in response to scrolling, depending on the `displayMode` that you set.

## Parameters

- `displayMode`: A control that indicates whether to hide   the search field in response to scrolling.

## See Also

- [static let automatic: SearchFieldPlacement](searchfieldplacement/automatic.md)
  SwiftUI places the search field automatically.
- [static let navigationBarDrawer: SearchFieldPlacement](searchfieldplacement/navigationbardrawer.md)
  The search field appears in the navigation bar.
- [static let sidebar: SearchFieldPlacement](searchfieldplacement/sidebar.md)
  The search field appears in the sidebar of a navigation view.
- [static let toolbar: SearchFieldPlacement](searchfieldplacement/toolbar.md)
  The search field appears in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement/navigationbardrawer(displaymode:))*