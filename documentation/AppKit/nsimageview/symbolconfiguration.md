# symbolConfiguration

**Framework**: AppKit  
**Kind**: property

Specifies a combination of point size, weight, and scale to use when sizing and displaying symbol images.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@NSCopying
var symbolConfiguration: NSImage.SymbolConfiguration? { get set }
```

#### Discussion

If a symbol configuration isn’t provided, the image view uses a default size, weight, and scale provided by the system. The default value is `nil`.

## See Also

- [var image: NSImage?](nsimageview/image.md)
  The image displayed by the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/symbolconfiguration)*