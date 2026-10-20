# overlayPreferenceValue(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

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
func overlayPreferenceValue<Key, T>(_ key: Key.Type = Key.self, @ContentBuilder _ transform: @escaping (Key.Value) -> T) -> some View where Key : PreferenceKey, T : View
```

#### Return Value

A view that layers a second view in front of the view.

## Parameters

- `key`: The preference key type whose value is to be read.
- `transform`: A function that produces the overlay view from the preference value read from the original view.

## See Also

### Generating backgrounds and overlays from preferences
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](./backgroundpreferencevalue%28_,_%29.md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](./backgroundpreferencevalue%28_,alignment,_%29.md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](./overlaypreferencevalue%28_,alignment,_%29.md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlaypreferencevalue(_:_:))*