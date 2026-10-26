---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/ongeometrychange(for:of:action:)-2zy6a"
framework: "CareKit/CareKitUI"
---

# onGeometryChange(for:of:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onGeometryChange(for:of:action:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
nonisolated func onGeometryChange<T>(for type: T.Type, of transform: @escaping @Sendable (GeometryProxy) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable, T : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/ongeometrychange(for:of:action:)-2zy6a)*