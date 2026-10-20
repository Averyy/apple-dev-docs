# subscript(section:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

The customization of the section, identified by its customization identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
subscript(section id: String) -> TabViewCustomization.SectionCustomization { get set }
```

#### Overview

Section tab order can be read by subscripting with the tab section’s id:

```swift
let order = customization[section: "com.myApp.categories"].tabOrder
```

To reset the order of an individual section, use [`resetTabOrder()`](./sectioncustomization/resettaborder%28%29.md). To reset the order of all sections, use [`resetSectionOrder()`](./resetsectionorder%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(section:))*