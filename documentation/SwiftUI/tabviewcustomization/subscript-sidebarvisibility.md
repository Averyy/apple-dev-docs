# subscript(sidebarVisibility:)

**Framework**: SwiftUI  
**Kind**: subscript

The visibility of the tab identified by its customization identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
subscript(sidebarVisibility id: String) -> Visibility { get set }
```

#### Overview

Visibility can be set imperatively by subscripting with the tab’s id:

```swift
customization[sidebarVisibility: "com.myApp.alerts"] = .hidden
```

You can change the default visibility by using the [`defaultVisibility(_:for:)`](tabcontent/defaultvisibility(_:for:).md) with a [`sidebar`](adaptabletabbarplacement/sidebar.md) placement.

```swift
Tab("Alerts", systemImage: "bell", value: .alerts) {
    AlertsView()
}
.customizationID("com.myApp.alerts")
.defaultVisibility(.hidden, for: .sidebar)
```

If the ID isn’t associated with a tab or the tab has not been customized, a default value of `.automatic` is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(sidebarvisibility:))*