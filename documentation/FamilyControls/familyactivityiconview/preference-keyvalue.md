# preference(key:value:)

**Framework**: FamilyControls  
**Kind**: method

Sets a value for the given preference.

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
func preference<K>(key: K.Type = K.self, value: K.Value) -> some View where K : PreferenceKey
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/preference(key:value:))*