# transformPreference(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Setting preferences
- [func preference<K>(key: K.Type, value: K.Value) -> some View](./preference%28key,value%29.md)
  Sets a value for the given preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transformpreference(_:_:))*