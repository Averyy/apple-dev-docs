# liveOff

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Type Property

Return an icon for identifying assets whose additional Live Photo content is disabled.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var liveOff: PHLivePhotoBadgeOptions { get }
```

```c
PHLivePhotoBadgeOptionsLiveOff
```

## Discussion

For example, when implementing a picker interface for sharing photos on a social network, you can use this icon to indicate when the user has chosen not to share the additional motion and sound content of a Live Photo.

## See Also

### Constants
- [static var overContent: PHLivePhotoBadgeOptions](./overcontent.md)
  Return a variant icon for use on a variable background such as an animating Live Photo view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions/liveoff)*