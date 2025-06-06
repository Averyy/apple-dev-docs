# collapsedRepresentationLabel

**Framework**: AppKit  
**Kind**: property

The localized string displayed by the button for the default collapsed representation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var collapsedRepresentationLabel: String { get set }
```

#### Discussion

If the [`collapsedRepresentation`](nspopovertouchbaritem/collapsedrepresentation.md) button has been replaced by a different view, this property may not have any effect.

## See Also

- [var collapsedRepresentation: NSView](nspopovertouchbaritem/collapsedrepresentation.md)
  The view displayed when this item is displayed in its parent bar.
- [var collapsedRepresentationImage: UIImage?](nspopovertouchbaritem/collapsedrepresentationimage.md)
  The image displayed by the button for the default collapsed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/collapsedrepresentationlabel)*