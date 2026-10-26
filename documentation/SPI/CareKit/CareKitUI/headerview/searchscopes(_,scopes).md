---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchscopes(_:scopes:)"
framework: "CareKit/CareKitUI"
---

# searchScopes(_:scopes:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchScopes(_:scopes:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.4+

## Declaration

```swift
nonisolated
func searchScopes<V, S>(_ scope: Binding<V>, @ViewBuilder scopes: () -> S) -> some View where V : Hashable, S : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchscopes(_:scopes:))*