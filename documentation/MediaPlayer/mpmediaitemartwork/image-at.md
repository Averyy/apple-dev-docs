# image(at:)

**Framework**: Media Player  
**Kind**: method

Returns the artwork image for an item at the given size.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func image(at size: CGSize) -> NSImage?
```

#### Return Value

The artwork at the requested size.

#### Discussion

The returned image is the smallest available image that’s at least as large as the requested size.

## Parameters

- `size`: The size, in points, for the new   object.

## See Also

- [iPod Library Access Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008765)
- [var bounds: CGRect](mpmediaitemartwork/bounds.md)
  The maximum size, in points, of the image associated with the media item artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/image(at:))*