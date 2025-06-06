# sectionActions(content:)

**Framework**: SwiftUI  
**Kind**: method

Adds custom actions to a section.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func sectionActions<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

On iOS, the actions are displayed as items after the content of the section. On macOS, the actions are displayed when a user hovers over the section.

The following example adds an ‘Add’ button to the ‘Categories’ section.

```swift
List {
    Label("Home", systemImage: "house")
    Label("Alerts", systemImage: "bell")

    Section("Categories") {
        Label("Climate", systemImage: "fan")
        Label("Lights", systemImage: "lightbulb")
    }
    .sectionActions {
        Button("Add Category", systemImage: "plus") { }
    }
}
```

## See Also

- [struct TabPlacement](tabplacement.md)
  A place that a tab can appear.
- [struct TabContentBuilder](tabcontentbuilder.md)
  A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [protocol TabContent](tabcontent.md)
  A type that provides content for programmatically selectable tabs in a tab view.
- [struct AnyTabContent](anytabcontent.md)
  Type erased tab content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sectionactions(content:))*