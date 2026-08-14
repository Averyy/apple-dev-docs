# CGImageSourceSetAllowableTypes(_:)

**Framework**: Image I/O  
**Kind**: func

Restricts which image formats can be decoded in the current process.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
func CGImageSourceSetAllowableTypes(_ allowableTypes: CFArray) -> OSStatus
```

#### Discussion

When this method has been called, ImageIO will only decode images whose format matches one of the entries in the allow list for the remaining lifetime of the process.

If per-asset format restrictions are set via [`kCGImageSourceAllowableTypes`](kcgimagesourceallowabletypes.md), only formats allowed by both mechanisms are permitted. If `allowableTypes` is empty, all image parsing is disabled. Unknown format identifiers are ignored. Can only be called once per process; subsequent calls are ignored.

See also [`System-declared uniform type identifiers`](https://developer.apple.com/documentation/uniformtypeidentifiers/system-declared-uniform-type-identifiers).

## Parameters

- `allowableTypes`: A [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) containing [`CFString`](https://developer.apple.com/documentation/corefoundation/cfstring) Uniform Type Identifiers (UTIs) of allowed image formats.

## See Also

- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](cgimagedestinationaddimageandmetadata(_:_:_:_:).md)
- [func CGImageDestinationCopyImageSource(CGImageDestination, CGImageSource, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](cgimagedestinationcopyimagesource(_:_:_:_:).md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](cgimagesourcecopymetadataatindex(_:_:_:).md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](cgimagesourceremovecacheatindex(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcesetallowabletypes(_:))*