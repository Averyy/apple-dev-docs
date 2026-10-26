---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onscrollgeometrychange(for:of:action:)"
framework: "CareKit/CareKitUI"
---

# onScrollGeometryChange(for:of:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onScrollGeometryChange(for:of:action:)`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func onScrollGeometryChange<T>(for type: T.Type, of transform: @escaping (ScrollGeometry) -> T, action: @escaping (T, T) -> Void) -> some View where T : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onscrollgeometrychange(for:of:action:))*