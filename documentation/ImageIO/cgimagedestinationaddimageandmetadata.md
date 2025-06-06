# CGImageDestinationAddImageAndMetadata(_:_:_:_:)

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
func CGImageDestinationAddImageAndMetadata(_ idst: CGImageDestination, _ image: CGImage, _ metadata: CGImageMetadata?, _ options: CFDictionary?)
```

## See Also

- [func CGImageDestinationCopyImageSource(CGImageDestination, CGImageSource, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](cgimagedestinationcopyimagesource(_:_:_:_:).md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](cgimagesourcecopymetadataatindex(_:_:_:).md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](cgimagesourceremovecacheatindex(_:_:).md)
- [func CGImageSourceSetAllowableTypes(CFArray) -> OSStatus](cgimagesourcesetallowabletypes(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationaddimageandmetadata(_:_:_:_:))*