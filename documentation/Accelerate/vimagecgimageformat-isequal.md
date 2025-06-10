# vImageCGImageFormat_IsEqual(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a Boolean value that indicates whether two vImage Core Graphics image formats are equal.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCGImageFormat_IsEqual(_ f1: UnsafePointer<vImage_CGImageFormat>!, _ f2: UnsafePointer<vImage_CGImageFormat>!) -> Bool
```

#### Return Value

A Boolean value that indicates whether two vImage Core Graphics image formats are equal.

## Parameters

- `f1`: The first   structure. If   is  , the function uses sRGB.
- `f2`: The second   structure. If   is  , the function uses sRGB.

## See Also

- [func vImageCGImageFormat_GetComponentCount(UnsafePointer<vImage_CGImageFormat>) -> UInt32](vimagecgimageformat_getcomponentcount(_:).md)
  Calculates the number of color and alpha channels for a specified image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecgimageformat_isequal(_:_:))*