# vImageCVImageFormat_Release

**Framework**: Accelerate  
**Kind**: func

Releases a Core Video image format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
void vImageCVImageFormat_Release(vImageCVImageFormatRef fmt);
```

#### Discussion

This function decrements the Core Video image format’s reference count. When the reference count reaches `0`, the system calls the `userDataReleaseCallback` (see [`vImageCVImageFormat_SetUserData(_:_:_:)`](vimagecvimageformat_setuserdata(_:_:_:).md)), and then destroys the object. The `userDataReleaseCallback` can access the [`vImageCVImageFormat`](vimagecvimageformat.md) object, but can’t prevent its destruction.

## Parameters

- `fmt`: The Core Video image format to release.

## See Also

- [vImageCVImageFormat_Retain](vimagecvimageformat_retain.md)
  Retains a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_release)*