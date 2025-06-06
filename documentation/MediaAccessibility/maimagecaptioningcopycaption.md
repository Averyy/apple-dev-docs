# MAImageCaptioningCopyCaption(_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Returns an accessibility caption from an image’s metadata.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func MAImageCaptioningCopyCaption(_ url: CFURL, _ error: UnsafeMutablePointer<CFError?>?) -> CFString?
```

## See Also

- [func MAImageCaptioningSetCaption(CFURL, CFString?, UnsafeMutablePointer<CFError?>?) -> Bool](maimagecaptioningsetcaption(_:_:_:).md)
  Sets the accessibility caption for an image’s metadata.
- [func MAImageCaptioningCopyMetadataTagPath() -> CFString](maimagecaptioningcopymetadatatagpath().md)
  Returns the metadata tag path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maimagecaptioningcopycaption(_:_:))*