# TabViewCustomization

**Framework**: SwiftUI  
**Kind**: struct

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

#### Overview

By default, if a person hasn’t made customizations, tabs appear according to the default builder visibilities and sections appear in the order you declare in the tab view’s tab builder.

You can change the default visibility by using the [`defaultVisibility(_:for:)`](tabcontent/defaultvisibility(_:for:).md) with a [`sidebar`](adaptabletabbarplacement/sidebar.md) placement.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [`resetTabOrder()`](tabviewcustomization/sectioncustomization/resettaborder().md) when you change the order.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [`disabled`](tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [`customizationBehavior(_:for:)`](tabcontent/customizationbehavior(_:for:).md).

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
- [TabViewCustomization.SectionCustomization](tabviewcustomization/sectioncustomization.md)
  The customizations a user has made to a [`TabSection`](tabsection.md).
- [TabViewCustomization.TabCustomization](tabviewcustomization/tabcustomization.md)
  The customizations a user has made to a [`Tab`](tab.md).
### Initializers
- [init()](tabviewcustomization/init.md)
  Creates an empty tab sidebar customization.
### Instance Methods
- [func resetSectionOrder()](tabviewcustomization/resetsectionorder.md)
  Resets ordering back to the default for all sections, preserving the customized tab visibilities.
- [func resetSectionOrder(for: String)](tabviewcustomization/resetsectionorder(for:).md)
  Resets ordering back to the default for the section with `sectionID`, preserving any customized tab visibilities.
- [func resetVisibility()](tabviewcustomization/resetvisibility.md)
  Resets all tab sidebar visibilities back to the default, preserving the section customizations.
### Subscripts
- [subscript(section _: String) -> TabViewCustomization.SectionCustomization](tabviewcustomization/subscript(section:).md)
  The customization of the section, identified by its customization identifier.
- [subscript(sectionID _: String) -> [String]?](tabviewcustomization/subscript(sectionid:).md)
  The customization for a section’s children, identified by the section’s customization identifier.
- [subscript(sidebarVisibility _: String) -> Visibility](tabviewcustomization/subscript(sidebarvisibility:).md)
  The visibility of the tab identified by its customization identifier.
- [subscript(tab _: String) -> TabViewCustomization.TabCustomization](tabviewcustomization/subscript(tab:).md)
  The customization of the tab, identified by its customization identifier.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](view/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [struct TabCustomizationBehavior](tabcustomizationbehavior.md)
  The customization behavior of customizable tab view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization)*