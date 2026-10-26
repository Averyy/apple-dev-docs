---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/overlaypreferencevalue(_:alignment:_:)"
framework: "CareKit/CareKitUI"
---

# overlayPreferenceValue(_:alignment:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.overlayPreferenceValue(_:alignment:_:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func overlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment = .center, @ViewBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/overlaypreferencevalue(_:alignment:_:))*