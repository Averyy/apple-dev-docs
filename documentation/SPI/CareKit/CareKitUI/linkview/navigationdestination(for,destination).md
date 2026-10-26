---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/navigationdestination(for:destination:)"
framework: "CareKit/CareKitUI"
---

# navigationDestination(for:destination:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.navigationDestination(for:destination:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDestination<D, C>(for data: D.Type, @ViewBuilder destination: @escaping (D) -> C) -> some View where D : Hashable, C : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/navigationdestination(for:destination:))*