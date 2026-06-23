# adornments

**Framework**: PaperKit  
**Kind**: property

An array of visual adornments that appear on the markup canvas.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var adornments: [MarkupAdornment] { get set }
```

#### Discussion

Adornments are supplementary visual elements you place on the canvas above the primary markup content. You position adornments using anchor points and configure them to respond to interaction, zoom scaling, and movement.

> **Note**: Adornments are expected to have unique IDs. If two or more adornments have the same ID, the system displays only one.

## See Also

- [func adornmentFrame(for: UUID) -> CGRect?](papermarkupviewcontroller/adornmentframe(for:).md)
  Returns the current frame of the specified adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/adornments)*