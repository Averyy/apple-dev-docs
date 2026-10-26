---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/contextmenu(forselectiontype:menu:primaryaction:)"
framework: "CareKit/CareKitUI"
---

# contextMenu(forSelectionType:menu:primaryAction:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.contextMenu(forSelectionType:menu:primaryAction:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func contextMenu<I, M>(forSelectionType itemType: I.Type = I.self, @ViewBuilder menu: @escaping (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)? = nil) -> some View where I : Hashable, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/contextmenu(forselectiontype:menu:primaryaction:))*