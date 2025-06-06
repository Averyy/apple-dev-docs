# CGImageDestinationCopyImageSource(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

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

## See Also

- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](cgimagedestinationaddimageandmetadata(_:_:_:_:).md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](cgimagesourcecopymetadataatindex(_:_:_:).md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](cgimagesourceremovecacheatindex(_:_:).md)
- [func CGImageSourceSetAllowableTypes(CFArray) -> OSStatus](cgimagesourcesetallowabletypes(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationcopyimagesource(_:_:_:_:))*