---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/contextmenu(menuitems:preview:)"
framework: "CareKit/CareKitUI"
---

# contextMenu(menuItems:preview:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.contextMenu(menuItems:preview:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
nonisolated
func contextMenu<M, P>(@ViewBuilder menuItems: () -> M, @ViewBuilder preview: () -> P) -> some View where M : View, P : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/contextmenu(menuitems:preview:))*