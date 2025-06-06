# customizationBehavior(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Configures the customization behavior of customizable tab view content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func customizationBehavior(_ behavior: TabCustomizationBehavior, for placements: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
```

#### Discussion

The [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style supports customization of the tab bar and sidebar on iPad. To enable customization, attach a [`TabViewCustomization`](tabviewcustomization.md) to the [`TabView`](tabview.md) using [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md).

This modifier has no effect on other platforms or on a [`TabViewStyle`](tabviewstyle.md) that doesn’t support customization.

Use this modifier to specify the customization behavior a person can perform on items in the specified placement. To enable customization, all tabs need a customization ID.

In the following example, the tabs support all of the different kinds of customizations in both the sidebar and tab bar.

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

You can create an item that cannot be hidden or moved by passing a value of [`disabled`](tabcustomizationbehavior/disabled.md) to this modifier. Only turn off customization for important tabs that people need for the app to do common functionality. If you turn off customization for both the sidebar and tab bar, then a customization ID isn’t necessary.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationBehavior(.disabled, for: .sidebar, .tabBar)

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

Pass a value of [`reorderable`](tabcustomizationbehavior/reorderable.md) to create an item that people can move, but can’t hide. In the [`sidebar`](adaptabletabbarplacement/sidebar.md), people can only reorder tabs within sections.

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
    .customizationBehavior(.reorderable, for: .sidebar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

You can individually customize each placement’s behavior. The following example would allow reordering of children in the sidebar but prohibit hiding or moving the tab in the tab bar.

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
    .customizationBehavior(.reorderable, for: .sidebar)
    .customizationBehavior(.disabled, for: .tabBar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## Parameters

- `behavior`: The customization behavior of the customizable   tab content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/customizationbehavior(_:for:))*