# vImageCGImageFormat_GetComponentCount(_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the number of color and alpha channels for a specified image format.

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
func vImageCGImageFormat_GetComponentCount(_ format: UnsafePointer<vImage_CGImageFormat>) -> UInt32
```

#### Return Value

The number of color and alpha channels in the image.

## Parameters

- `format`: A valid   structure.

## See Also

- [func vImageCGImageFormat_IsEqual(UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<vImage_CGImageFormat>!) -> Bool](vimagecgimageformat_isequal(_:_:).md)
  Returns a Boolean value that indicates whether two vImage Core Graphics image formats are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecgimageformat_getcomponentcount(_:))*