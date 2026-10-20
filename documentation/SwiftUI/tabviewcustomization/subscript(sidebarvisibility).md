# subscript(sidebarVisibility:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

The visibility of the tab identified by its customization identifier.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+ - Deprecated in 27.2
- macOS 15.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use the `tab` subscript and read `sidebarVisibility` instead.

## Declaration

```swift
subscript(sidebarVisibility id: String) -> Visibility { get set }
```

#### Overview

Visibility can be set imperatively by subscripting with the tab’s id:

```swift
customization[sidebarVisibility: "com.myApp.alerts"] = .hidden
```

You can change the default visibility by using the [`defaultVisibility(_:for:)`](../tabcontent/defaultvisibility%28_,for%29.md) with a [`sidebar`](../adaptabletabbarplacement/sidebar.md) placement.

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