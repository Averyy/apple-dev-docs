# CGImageRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern CGImageRefCGImageRetain(CGImageRef image);
```

## Return Value

The same image you passed in as the `image` parameter.

## Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `image` parameter is `NULL`.

## Parameters

- `image`: The image to retain.

## See Also

### Retaining and releasing images
- [CGImageRelease](./cgimagerelease.md)
  Decrements the retain count of a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimageretain)*