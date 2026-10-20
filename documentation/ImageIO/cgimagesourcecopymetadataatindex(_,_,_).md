# CGImageSourceCopyMetadataAtIndex(_:_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CGImageMetadata?
```

```c
extern CGImageMetadataRefCGImageSourceCopyMetadataAtIndex(CGImageSourceRef isrc, size_t index, CFDictionaryRef options);
```

## See Also

### Functions
- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](./cgimagedestinationaddimageandmetadata%28_,_,_,_%29.md)
- [func CGImageDestinationCopyImageSource(CGImageDestination, CGImageSource, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./cgimagedestinationcopyimagesource%28_,_,_,_%29.md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](./cgimagesourceremovecacheatindex%28_,_%29.md)
- [func CGImageSourceSetAllowableTypes(CFArray) -> OSStatus](./cgimagesourcesetallowabletypes%28_%29.md)
  Restricts which image formats can be decoded in the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecopymetadataatindex(_:_:_:))*