# imageView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image view that the scrubber item uses to display its image.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var imageView: NSImageView { get }
```

```objc
@property (strong, readonly) NSImageView * imageView;
```

## Discussion

Use this property to access and configure the underlying image view used to display the image in the [`image`](./image.md) property.

## See Also

### Providing image content
- [var image: NSImage](./image.md)
  The image displayed by the scrubber item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberimageitemview/imageview)*