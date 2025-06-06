# tabOrder

**Framework**: SwiftUI  
**Kind**: property

The order customization for the tabs in a section, identified by customization identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var tabOrder: [String]? { get }
```

#### Discussion

Identifiers can be associated with a `Tab` or `TabSection` using the `customizationID(_:)` modifier.

```swift
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
```

Section tab order can be read by subscripting the customization with the tab section’s id:

```swift
let order = customization[section: "com.myApp.categories"].tabOrder
```

If the section has been customized, this returns the current order for all the tabs in the section, including tabs that have not been customized. If the section has not been customized or the identifier does not correspond to a section, the order will be nil to indicate the tab order matches that of the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/sectioncustomization/taborder)*