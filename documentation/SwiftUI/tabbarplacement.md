# TabBarPlacement

**Framework**: SwiftUI  
**Kind**: struct

A placement for tabs in a tab view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TabBarPlacement
```

## Topics

### Type Properties
- [static let bottomBar: TabBarPlacement](tabbarplacement/bottombar.md)
  Bottom bar of a tab view.
- [static let ornament: TabBarPlacement](tabbarplacement/ornament.md)
  Tab view displaying as an ornament.
- [static let pageIndicator: TabBarPlacement](tabbarplacement/pageindicator.md)
  Tab view displaying as an indicator that shows the position within the pages.
- [static let sidebar: TabBarPlacement](tabbarplacement/sidebar.md)
  The sidebar of a tab view.
- [static let topBar: TabBarPlacement](tabbarplacement/topbar.md)
  Top bar of a tab view.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](view/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [struct AdaptableTabBarPlacement](adaptabletabbarplacement.md)
  A placement for tabs in a tab view using the adaptable sidebar style.
- [var tabBarPlacement: TabBarPlacement?](environmentvalues/tabbarplacement.md)
  The current placement of the tab bar.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [struct TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [enum TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md)
  A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabbarplacement)*