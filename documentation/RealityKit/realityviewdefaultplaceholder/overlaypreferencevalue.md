# overlayPreferenceValue(_:_:)

**Framework**: RealityKit  
**Kind**: method

Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func overlayPreferenceValue<Key, T>(_ key: Key.Type = Key.self, @ViewBuilder _ transform: @escaping (Key.Value) -> T) -> some View where Key : PreferenceKey, T : View
```

#### Return Value

A view that layers a second view in front of the view.

## Parameters

- `key`: The preference key type whose value is to be read.
- `transform`: A function that produces the overlay view from   the preference value read from the original view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/overlaypreferencevalue(_:_:))*