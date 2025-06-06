# customizationID(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the identifier for a tab to persist its state.

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
nonisolated
func customizationID(_ id: String) -> some TabContent<Self.TabValue>
```

#### Discussion

The identifier needs to be stable, including across app version updates.

Only the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style supports supports customization. To enable customization, attach a [`TabViewCustomization`](tabviewcustomization.md) to the [`TabView`](tabview.md) using [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md).

All tabs and tab sections that support customization are required to have a customization ID. You can mark a tab as being non-customizable by specifying a [`disabled`](tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [`customizationBehavior(_:for:)`](tabcontent/customizationbehavior(_:for:).md).

If you apply a customization ID to a [`TabSection`](tabsection.md), ensure you specify customization IDs for all of the tabs within the section, unless the tab has been marked as having customization turned off.

The following example adds customization identifiers to all tabs and tab sections.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }
        .customizationID("com.myApp.climate")

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
        .customizationID("com.myApp.lights")
    }
    .customizationID("com.myApp.categories")
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## Parameters

- `id`: The identifier to associate with a tab or section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/customizationid(_:))*