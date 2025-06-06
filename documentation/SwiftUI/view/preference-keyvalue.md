# preference(key:value:)

**Framework**: SwiftUI  
**Kind**: method

Sets a value for the given preference.

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
func preference<K>(key: K.Type = K.self, value: K.Value) -> some View where K : PreferenceKey
```

## See Also

- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](view/transformpreference(_:_:).md)
  Applies a transformation to a preference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/preference(key:value:))*