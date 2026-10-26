---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchscopes(_:activation:_:)"
framework: "CareKit/CareKitUI"
---

# searchScopes(_:activation:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchScopes(_:activation:_:)`.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+

## Declaration

```swift
nonisolated
func searchScopes<V, S>(_ scope: Binding<V>, activation: SearchScopeActivation, @ViewBuilder _ scopes: () -> S) -> some View where V : Hashable, S : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchscopes(_:activation:_:))*