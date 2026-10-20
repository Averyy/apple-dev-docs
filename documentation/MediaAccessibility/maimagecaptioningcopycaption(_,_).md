# MAImageCaptioningCopyCaption(_:_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

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

```c
extern CFStringRefMAImageCaptioningCopyCaption(CFURLRef url, CFErrorRef*error);
```

## See Also

### Image captioning settings
- [func MAImageCaptioningSetCaption(CFURL, CFString?, UnsafeMutablePointer<CFError?>?) -> Bool](./maimagecaptioningsetcaption%28_,_,_%29.md)
  Sets the accessibility caption for an image’s metadata.
- [func MAImageCaptioningCopyMetadataTagPath() -> CFString](./maimagecaptioningcopymetadatatagpath%28%29.md)
  Returns the metadata tag path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maimagecaptioningcopycaption(_:_:))*