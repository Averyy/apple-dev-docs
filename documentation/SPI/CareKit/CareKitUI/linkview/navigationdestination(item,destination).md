---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/navigationdestination(item:destination:)"
framework: "CareKit/CareKitUI"
---

# navigationDestination(item:destination:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.navigationDestination(item:destination:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func navigationDestination<D, C>(item: Binding<Optional<D>>, @ViewBuilder destination: @escaping (D) -> C) -> some View where D : Hashable, C : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/navigationdestination(item:destination:))*