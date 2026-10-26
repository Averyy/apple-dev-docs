---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onpreferencechange(_:perform:)"
framework: "CareKit/CareKitUI"
---

# onPreferenceChange(_:perform:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onPreferenceChange(_:perform:)`.

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
func onPreferenceChange<K>(_ key: K.Type = K.self, perform action: @escaping (K.Value) -> Void) -> some View where K : PreferenceKey, K.Value : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onpreferencechange(_:perform:))*