---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/transformanchorpreference(key:value:transform:)"
framework: "CareKit/CareKitUI"
---

# transformAnchorPreference(key:value:transform:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.transformAnchorPreference(key:value:transform:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformAnchorPreference<A, K>(key _: K.Type = K.self, value: Anchor<A>.Source, transform: @escaping (inout K.Value, Anchor<A>) -> Void) -> some View where K : PreferenceKey
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/transformanchorpreference(key:value:transform:))*