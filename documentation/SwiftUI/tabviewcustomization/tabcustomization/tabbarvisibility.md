# tabBarVisibility

**Framework**: SwiftUI  
**Kind**: property

The visibility of the tab in the tab bar.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var tabBarVisibility: Visibility { get }
```

#### Discussion

You can change the default visibility by using the `TabContent/defaultVisibility(_:for)` with a `AdaptableTabBarPlacement.tabBar` placement.

If the ID isn’t associated with a tab or the tab has not been customized, a default value of `.automatic` is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/tabcustomization/tabbarvisibility)*