# focusScope(_:)

**Framework**: MusicKit  
**Kind**: method

Creates a focus scope that SwiftUI uses to limit default focus preferences.

**Availability**:
- macOS 12.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func focusScope(_ namespace: Namespace.ID) -> some View
```

#### Return Value

A view that sets the namespace of descendants for default focus.

#### Discussion

The returned view gets associated with the provided namespace. Pass this namespace to `View/prefersDefaultFocus(_:in:)` and the `EnvironmentValues/resetFocus` function.

## Parameters

- `namespace`: A namespace identifier that SwiftUI can use to scope   default focus preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/focusscope(_:))*