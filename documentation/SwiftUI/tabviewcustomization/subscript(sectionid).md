# subscript(sectionID:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

The customization for a section’s children, identified by the section’s customization identifier.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+ - Deprecated in 27.2
- macOS 15.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use the `section` subscript and read `tabOrder` instead.

## Declaration

```swift
subscript(sectionID id: String) -> [String]? { get }
```

## Overview

Section order can be read by subscripting with the tab section’s id:

```swift
let order = customization[sectionID: "com.myApp.categories"]
```

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

If the ID isn’t associated with a section or the section has not been customized, a default value of `nil` is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(sectionid:))*