# subscript(tab:)

**Framework**: SwiftUI  
**Kind**: subscript

The customization of the tab, identified by its customization identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
subscript(tab id: String) -> TabViewCustomization.TabCustomization { get set }
```

#### Overview

You can imperatively set properties by subscripting with the tab ID. The following example sets the tab’s sidebar visibility:

```swift
customization[tab: "com.myApp.alerts"].sidebarVisibility = .hidden
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(tab:))*