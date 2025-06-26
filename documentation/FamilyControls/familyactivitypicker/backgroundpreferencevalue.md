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

## See Also

- [func preference<K>(key: K.Type, value: K.Value) -> some View](familyactivitypicker/preference(key:value:).md)
  Sets a value for the given preference.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](familyactivitypicker/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](familyactivitypicker/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](familyactivitypicker/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](familyactivitypicker/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](familyactivitypicker/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/backgroundpreferencevalue(_:_:))*