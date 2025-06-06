# vImageCVImageFormat_GetUserData(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the user data of a Core Video image format.

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
func vImageCVImageFormat_GetUserData(_ format: vImageConstCVImageFormat) -> UnsafeMutableRawPointer!
```

#### Return Value

The address of `userData;` `NULL` if `userData` isn’t set.

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetUserData(_:)`](vimagecvimageformat_getuserdata(_:).md):

```swift
let userData = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetUserData(format)
}
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

- [func vImageCVImageFormat_SetUserData(vImageCVImageFormat, UnsafeMutableRawPointer!, ((vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Void)!) -> vImage_Error](vimagecvimageformat_setuserdata(_:_:_:).md)
  Sets the user data of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getuserdata(_:))*