# transformAnchorPreference(key:value:transform:)

**Framework**: RealityKit  
**Kind**: method

Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformAnchorPreference<A, K>(key _: K.Type = K.self, value: Anchor<A>.Source, transform: @escaping (inout K.Value, Anchor<A>) -> Void) -> some View where K : PreferenceKey
```

#### Return Value

A new version of the view that writes the preference.

## Parameters

- `key`: The preference key type.
- `value`: The geometry value in the current coordinate space.
- `transform`: The function to produce the preference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/transformanchorpreference(key:value:transform:))*