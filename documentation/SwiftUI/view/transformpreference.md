# transformPreference(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Applies a transformation to a preference value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformPreference<K>(_ key: K.Type = K.self, _ callback: @escaping (inout K.Value) -> Void) -> some View where K : PreferenceKey
```

## See Also

- [func preference<K>(key: K.Type, value: K.Value) -> some View](view/preference(key:value:).md)
  Sets a value for the given preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transformpreference(_:_:))*