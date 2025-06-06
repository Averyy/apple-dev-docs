# mask(_:)

**Framework**: App Intents  
**Kind**: method

Masks this view using the alpha channel of the given view.

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
func mask<Mask>(_ mask: Mask) -> some View where Mask : View
```

#### Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask(Rectangle().opacity(0.1))
```

## Parameters

- `mask`: The view whose alpha the rendering system applies to   the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/mask(_:))*