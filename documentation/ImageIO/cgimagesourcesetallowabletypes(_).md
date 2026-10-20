# CGImageSourceSetAllowableTypes(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CGImageSourceSetAllowableTypes(CFArrayRef allowableTypes);
```

#### Discussion

When this method has been called, ImageIO will only decode images whose format matches one of the entries in the allow list for the remaining lifetime of the process.

If per-asset format restrictions are set via [`kCGImageSourceAllowableTypes`](./kcgimagesourceallowabletypes.md), only formats allowed by both mechanisms are permitted. If `allowableTypes` is empty, all image parsing is disabled. Unknown format identifiers are ignored. Can only be called once per process; subsequent calls are ignored.

See also [System-declared uniform type identifiers](../UniformTypeIdentifiers/system-declared-uniform-type-identifiers.md).

## Parameters

- `allowableTypes`: A [`CFArray`](../CoreFoundation/cfarray.md) containing [`CFString`](../CoreFoundation/cfstring.md) Uniform Type Identifiers (UTIs) of allowed image formats.

## See Also

### Functions
- [func CGImageDestinationAddImageAndMetadata(CGImageDestination, CGImage, CGImageMetadata?, CFDictionary?)](./cgimagedestinationaddimageandmetadata%28_,_,_,_%29.md)
- [func CGImageDestinationCopyImageSource(CGImageDestination, CGImageSource, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./cgimagedestinationcopyimagesource%28_,_,_,_%29.md)
- [func CGImageSourceCopyMetadataAtIndex(CGImageSource, Int, CFDictionary?) -> CGImageMetadata?](./cgimagesourcecopymetadataatindex%28_,_,_%29.md)
- [func CGImageSourceRemoveCacheAtIndex(CGImageSource, Int)](./cgimagesourceremovecacheatindex%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcesetallowabletypes(_:))*