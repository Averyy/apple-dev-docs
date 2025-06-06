# transformPreference(_:_:)

**Framework**: FinanceKitUI  
**Kind**: method

Applies a transformation to a preference value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/transformpreference(_:_:))*