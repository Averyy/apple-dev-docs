# backgroundPreferenceValue(_:_:)

**Framework**: FamilyControls  
**Kind**: method

Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func backgroundPreferenceValue<Key, T>(_ key: Key.Type = Key.self, @ViewBuilder _ transform: @escaping (Key.Value) -> T) -> some View where Key : PreferenceKey, T : View
```

#### Return Value

A view that layers a second view behind the view.

## Parameters

- `key`: The preference key type whose value is to be read.
- `transform`: A function that produces the background view from   the preference value read from the original view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/backgroundpreferencevalue(_:_:))*