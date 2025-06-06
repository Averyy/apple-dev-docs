# Preview(_:traits:body:)

**Framework**: AppKit  
**Kind**: macro

Preview an NSView.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @PreviewMacroBodyBuilder<NSView> body: @escaping @MainActor () -> NSView)
```

## Parameters

- `name`: Optional display name for the preview, which will appear in the canvas.
- `traits`: Optional list of traits customizing the appearance of the preview.
- `body`: A closure producing an NSView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/preview(_:traits:body:)-7pfjp)*