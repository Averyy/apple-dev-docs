# useHardwareAcceleration

**Framework**: Core Image  
**Kind**: property

A Boolean value specifying that using hardware is preferred when decoding.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let useHardwareAcceleration: CIImageOption
```

#### Discussion

If the value for this option is:

- True: The image will be decoded using dedicated hardware if possible.
- False: The image will be decoded using the CPU is possible.
- Not specified: The default behavior is True.

This option is only supported by JPEG and HEIF images formats.

This option is only supported by these APIs:

- `/CIImage/imageWithContentsOfURL:options:`
- `/CIImage/initWithContentsOfURL:options:`
- `/CIImage/imageWithData:options:`
- `/CIImage/initWithData:options:`
- `/CIImage/imageWithCGImageSource:index:options:`
- `/CIImage/initWithCGImageSource:index:options:`

> **Note**: The `kCGImageSourceUseHardwareAcceleration` key can also be used for this purpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/usehardwareacceleration)*