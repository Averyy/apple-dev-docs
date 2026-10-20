# MAImageCaptioningSetCaption(_:_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Sets the accessibility caption for an image’s metadata.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func MAImageCaptioningSetCaption(_ url: CFURL, _ string: CFString?, _ error: UnsafeMutablePointer<CFError?>?) -> Bool
```

## See Also

- [func MAImageCaptioningCopyCaption(CFURL, UnsafeMutablePointer<CFError?>?) -> CFString?](maimagecaptioningcopycaption(_:_:).md)
  Returns an accessibility caption from an image’s metadata.
- [func MAImageCaptioningCopyMetadataTagPath() -> CFString](maimagecaptioningcopymetadatatagpath().md)
  Returns the metadata tag path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maimagecaptioningsetcaption(_:_:_:))*