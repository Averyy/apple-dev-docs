# AdaptableTabBarPlacement

**Framework**: SwiftUI  
**Kind**: struct

A placement for tabs in a tab view using the adaptable sidebar style.

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
struct AdaptableTabBarPlacement
```

## Topics

### Type Properties
- [static let automatic: AdaptableTabBarPlacement](adaptabletabbarplacement/automatic.md)
  The automatic placement.
- [static let sidebar: AdaptableTabBarPlacement](adaptabletabbarplacement/sidebar.md)
  The sidebar of a tab view.
- [static let tabBar: AdaptableTabBarPlacement](adaptabletabbarplacement/tabbar.md)
  The tab bar of a tab view.

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
- [var tabBarPlacement: TabBarPlacement?](environmentvalues/tabbarplacement.md)
  The current placement of the tab bar.
- [struct TabBarPlacement](tabbarplacement.md)
  A placement for tabs in a tab view.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [struct TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [enum TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md)
  A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/adaptabletabbarplacement)*