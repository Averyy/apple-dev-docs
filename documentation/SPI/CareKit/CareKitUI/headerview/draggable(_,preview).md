---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/draggable(_:preview:)"
framework: "CareKit/CareKitUI"
---

# draggable(_:preview:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.draggable(_:preview:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func draggable<V, T>(_ payload: @autoclosure @escaping () -> T, @ViewBuilder preview: () -> V) -> some View where V : View, T : Transferable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/draggable(_:preview:))*