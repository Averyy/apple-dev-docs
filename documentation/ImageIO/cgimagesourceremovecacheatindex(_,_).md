# CGImageSourceRemoveCacheAtIndex(_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource, _ index: Int)
```

```c
extern void CGImageSourceRemoveCacheAtIndex(CGImageSourceRef isrc, size_t index);
```

## See Also

### Functions
- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](./cgimagedestinationaddimageandmetadata%28_,_,_,_%29.md)
- [func CGImageDestinationCopyImageSource(CGImageDestination, CGImageSource, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./cgimagedestinationcopyimagesource%28_,_,_,_%29.md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](./cgimagesourcecopymetadataatindex%28_,_,_%29.md)
- [func CGImageSourceSetAllowableTypes(CFArray) -> OSStatus](./cgimagesourcesetallowabletypes%28_%29.md)
  Restricts which image formats can be decoded in the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourceremovecacheatindex(_:_:))*