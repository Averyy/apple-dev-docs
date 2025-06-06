# vImageCVImageFormat_SetUserData(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the user data of a Core Video image format.

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
func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutableRawPointer!, _ userDataReleaseCallback: ((vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Void)!) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

## Parameters

- `format`: The Core Video image format to update.
- `userData`: The new user data for the format.
- `userDataReleaseCallback`: The callback the system calls when it releases the   instance or overwrites the   pointer.

## See Also

- [func vImageCVImageFormat_GetUserData(vImageConstCVImageFormat) -> UnsafeMutableRawPointer!](vimagecvimageformat_getuserdata(_:).md)
  Returns the user data of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_setuserdata(_:_:_:))*