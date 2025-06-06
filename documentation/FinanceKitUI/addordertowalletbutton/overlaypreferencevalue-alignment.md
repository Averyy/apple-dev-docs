# overlayPreferenceValue(_:alignment:_:)

**Framework**: FinanceKitUI  
**Kind**: method

Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func overlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment = .center, @ViewBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View
```

#### Return Value

A view that layers a second view in front of the view.

#### Discussion

The values of the preference key from both views are combined and made visible to the parent view.

## Parameters

- `key`: The preference key type whose value is to be read.
- `alignment`: An optional alignment to use when positioning the   overlay view relative to the original view.
- `transform`: A function that produces the overlay view from   the preference value read from the original view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/overlaypreferencevalue(_:alignment:_:))*