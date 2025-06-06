# mask(alignment:_:)

**Framework**: FinanceKitUI  
**Kind**: method

Masks this view using the alpha channel of the given view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func mask<Mask>(alignment: Alignment = .center, @ViewBuilder _ mask: () -> Mask) -> some View where Mask : View
```

#### Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```None
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask {
        Rectangle().opacity(0.1)
    }
```

## Parameters

- `alignment`: The alignment for   in relation to this view.
- `mask`: The view whose alpha the rendering system applies to   the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/mask(alignment:_:))*