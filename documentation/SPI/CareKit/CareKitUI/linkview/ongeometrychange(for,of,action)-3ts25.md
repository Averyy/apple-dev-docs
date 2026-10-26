---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/ongeometrychange(for:of:action:)-3ts25"
framework: "CareKit/CareKitUI"
---

# onGeometryChange(for:of:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onGeometryChange(for:of:action:)`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
nonisolated func onGeometryChange<T>(for type: T.Type, of transform: @escaping @Sendable (GeometryProxy) -> T, action: @escaping (T, T) -> Void) -> some View where T : Equatable, T : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/ongeometrychange(for:of:action:)-3ts25)*