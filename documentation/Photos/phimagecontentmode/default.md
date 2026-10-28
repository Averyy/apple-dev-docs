# default

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

Fits the image to the requested size using the default option, [`PHImageContentMode.aspectFit`](./aspectfit.md).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var `default`: PHImageContentMode { get }
```

```c
PHImageContentModeDefault
```

## Discussion

Use this content mode when requesting a full-sized image using the [`PHImageManagerMaximumSize`](../phimagemanagermaximumsize.md) value for the target size. In this case, the image manager does not scale or crop the image.

## See Also

### Constants
- [PHImageContentMode.aspectFit](./aspectfit.md)
  Scales the image so that its larger dimension fits the target size.
- [PHImageContentMode.aspectFill](./aspectfill.md)
  Scales the image so that it completely fills the target size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagecontentmode/default)*