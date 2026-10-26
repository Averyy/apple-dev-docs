---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/backgroundpreferencevalue(_:_:)"
framework: "CareKit/CareKitUI"
---

# backgroundPreferenceValue(_:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.backgroundPreferenceValue(_:_:)`.

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
func backgroundPreferenceValue<Key, T>(_ key: Key.Type = Key.self, @ViewBuilder _ transform: @escaping (Key.Value) -> T) -> some View where Key : PreferenceKey, T : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/backgroundpreferencevalue(_:_:))*