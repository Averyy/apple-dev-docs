# TabBarMinimizeBehavior

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct TabBarMinimizeBehavior
```

## Topics

### Type Properties
- [static let automatic: TabBarMinimizeBehavior](tabbarminimizebehavior/automatic.md)
  Determine the behavior automatically based on the surrounding context.
- [static let never: TabBarMinimizeBehavior](tabbarminimizebehavior/never.md)
  Never minimize the tab bar.
- [static let onScrollDown: TabBarMinimizeBehavior](tabbarminimizebehavior/onscrolldown.md)
  Minimize the tab bar when downwards scrolling starts. Minimizing is supported for tab bars on only iPhone.
- [static let onScrollUp: TabBarMinimizeBehavior](tabbarminimizebehavior/onscrollup.md)
  Minimize the tab bar when upwards scrolling starts. Minimizing is supported for tab bars on only iPhone.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [struct TabBarPlacement](tabbarplacement.md)
  A placement for tabs in a tab view.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [enum TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md)
  A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior)*