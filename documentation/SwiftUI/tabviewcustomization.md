# TabViewCustomization

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The customizations a person makes to an adaptable sidebar tab view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct TabViewCustomization
```

## Overview

By default, if a person hasn’t made customizations, tabs appear according to the default builder visibilities and sections appear in the order you declare in the tab view’s tab builder.

You can change the default visibility by using the [`defaultVisibility(_:for:)`](./tabcontent/defaultvisibility%28_,for%29.md) with a [`sidebar`](./adaptabletabbarplacement/sidebar.md) placement.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [`resetTabOrder()`](./tabviewcustomization/sectioncustomization/resettaborder%28%29.md) when you change the order.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [`disabled`](./tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [`customizationBehavior(_:for:)`](./tabcontent/customizationbehavior%28_,for%29.md).

On macOS, a default interaction is provided for reordering sections but not for controlling the visibility of individual tabs. A custom experience should be provided if desired by setting the visibility of the tab on the customization.

The following code example uses `@AppStorage` to automatically persist any visibility or section order customizations a person makes.

```swift
@AppStorage
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        MyHomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Reports", systemImage: "chart.bar") {
        MyReportsView()
    }
    .customizationID("com.myApp.reports")

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
    .customizationID("com.myApp.browse")
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## Topics

### Structures
- [TabViewCustomization.SectionCustomization](./tabviewcustomization/sectioncustomization.md)
  The customizations a user has made to a [`TabSection`](./tabsection.md).
- [TabViewCustomization.TabCustomization](./tabviewcustomization/tabcustomization.md)
  The customizations a user has made to a [`Tab`](./tab.md).
### Initializers
- [init()](./tabviewcustomization/init%28%29.md)
  Creates an empty tab sidebar customization.
### Instance Methods
- [func resetSectionOrder()](./tabviewcustomization/resetsectionorder%28%29.md)
  Resets ordering back to the default for all sections, preserving the customized tab visibilities.
- [func resetSectionOrder(for: String)](./tabviewcustomization/resetsectionorder%28for%29.md)
  Resets ordering back to the default for the section with `sectionID`, preserving any customized tab visibilities.
- [func resetVisibility()](./tabviewcustomization/resetvisibility%28%29.md)
  Resets all tab sidebar visibilities back to the default, preserving the section customizations.
### Subscripts
- [subscript(section _: String) -> TabViewCustomization.SectionCustomization](./tabviewcustomization/subscript%28section%29.md)
  The customization of the section, identified by its customization identifier.
- [subscript(sectionID _: String) -> [String]?](./tabviewcustomization/subscript%28sectionid%29.md)
  The customization for a section’s children, identified by the section’s customization identifier.
- [subscript(sidebarVisibility _: String) -> Visibility](./tabviewcustomization/subscript%28sidebarvisibility%29.md)
  The visibility of the tab identified by its customization identifier.
- [subscript(tab _: String) -> TabViewCustomization.TabCustomization](./tabviewcustomization/subscript%28tab%29.md)
  The customization of the tab, identified by its customization identifier.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enabling tab customization
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](./view/tabviewcustomization%28_%29.md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [struct TabCustomizationBehavior](./tabcustomizationbehavior.md)
  The customization behavior of customizable tab view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization)*