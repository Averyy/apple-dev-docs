---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/transformpreference(_:_:)"
framework: "CareKit/CareKitUI"
---

# transformPreference(_:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.transformPreference(_:_:)`.

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
func transformPreference<K>(_ key: K.Type = K.self, _ callback: @escaping (inout K.Value) -> Void) -> some View where K : PreferenceKey
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/transformpreference(_:_:))*