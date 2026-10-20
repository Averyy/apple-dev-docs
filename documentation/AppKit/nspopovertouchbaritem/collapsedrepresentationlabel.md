# collapsedRepresentationLabel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The localized string displayed by the button for the default collapsed representation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var collapsedRepresentationLabel: String { get set }
```

```objc
@property (strong) NSString * collapsedRepresentationLabel;
```

#### Discussion

If the [`collapsedRepresentation`](./collapsedrepresentation.md) button has been replaced by a different view, this property may not have any effect.

## See Also

### Configuring the collapsed popover
- [var collapsedRepresentation: NSView](./collapsedrepresentation.md)
  The view displayed when this item is displayed in its parent bar.
- [var collapsedRepresentationImage: UIImage?](./collapsedrepresentationimage.md)
  The image displayed by the button for the default collapsed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/collapsedrepresentationlabel)*