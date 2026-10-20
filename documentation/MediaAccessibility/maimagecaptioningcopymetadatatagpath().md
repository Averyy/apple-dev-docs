# MAImageCaptioningCopyMetadataTagPath()

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the metadata tag path.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func MAImageCaptioningCopyMetadataTagPath() -> CFString
```

```c
extern CFStringRefMAImageCaptioningCopyMetadataTagPath();
```

## See Also

### Image captioning settings
- [func MAImageCaptioningCopyCaption(CFURL, UnsafeMutablePointer<CFError?>?) -> CFString?](./maimagecaptioningcopycaption%28_,_%29.md)
  Returns an accessibility caption from an image’s metadata.
- [func MAImageCaptioningSetCaption(CFURL, CFString?, UnsafeMutablePointer<CFError?>?) -> Bool](./maimagecaptioningsetcaption%28_,_,_%29.md)
  Sets the accessibility caption for an image’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maimagecaptioningcopymetadatatagpath())*