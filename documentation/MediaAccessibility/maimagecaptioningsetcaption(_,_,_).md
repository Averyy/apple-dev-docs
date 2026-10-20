# MAImageCaptioningSetCaption(_:_:_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

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

```c
extern bool MAImageCaptioningSetCaption(CFURLRef url, CFStringRef string, CFErrorRef*error);
```

## See Also

### Image captioning settings
- [func MAImageCaptioningCopyCaption(CFURL, UnsafeMutablePointer<CFError?>?) -> CFString?](./maimagecaptioningcopycaption%28_,_%29.md)
  Returns an accessibility caption from an image’s metadata.
- [func MAImageCaptioningCopyMetadataTagPath() -> CFString](./maimagecaptioningcopymetadatatagpath%28%29.md)
  Returns the metadata tag path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maimagecaptioningsetcaption(_:_:_:))*