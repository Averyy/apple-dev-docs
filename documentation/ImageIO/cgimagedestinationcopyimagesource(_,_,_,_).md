# CGImageDestinationCopyImageSource(_:_:_:_:)

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
func CGImageDestinationCopyImageSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ options: CFDictionary?, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

```c
extern bool CGImageDestinationCopyImageSource(CGImageDestinationRef idst, CGImageSourceRef isrc, CFDictionaryRef options, CFErrorRef*err);
```

## See Also

### Functions
- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](./cgimagedestinationaddimageandmetadata%28_,_,_,_%29.md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](./cgimagesourcecopymetadataatindex%28_,_,_%29.md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](./cgimagesourceremovecacheatindex%28_,_%29.md)
- [func CGImageSourceSetAllowableTypes(CFArray) -> OSStatus](./cgimagesourcesetallowabletypes%28_%29.md)
  Restricts which image formats can be decoded in the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationcopyimagesource(_:_:_:_:))*