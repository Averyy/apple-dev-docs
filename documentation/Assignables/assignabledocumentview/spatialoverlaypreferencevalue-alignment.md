# spatialOverlayPreferenceValue(_:alignment:_:)

**Framework**: Assignables  
**Kind**: method

Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func spatialOverlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment3D = .center, @ViewBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/spatialoverlaypreferencevalue(_:alignment:_:))*