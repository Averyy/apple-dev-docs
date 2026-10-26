# overContent

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Type Property

Return a variant icon for use on a variable background such as an animating Live Photo view.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var overContent: PHLivePhotoBadgeOptions { get }
```

```c
PHLivePhotoBadgeOptionsOverContent
```

#### Discussion

By default, the [`livePhotoBadgeImage(options:)`](../phlivephotoview/livephotobadgeimage%28options%29.md) returns a solid-color image suitable for use as a template image, which you can then tint for appropriate display against a specific background. If the background content is busy, animated, or unknown, add this option to instead obtain an icon (not suitable for use as a template image) that provides extra contrast for better readability.

## See Also

### Constants
- [static var liveOff: PHLivePhotoBadgeOptions](./liveoff.md)
  Return an icon for identifying assets whose additional Live Photo content is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions/overcontent)*