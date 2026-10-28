# imageRepWithCIImage:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a representation of an image initialized to the specified Core Image instance.

**Availability**:
- macOS

## Declaration

```objc
+ (instancetype) imageRepWithCIImage:(CIImage *) image;
```

## Return Value

An initialized [`NSCIImageRep`](../nsciimagerep.md) object, or `nil` if the object could not be initialized.

## Parameters

- `image`: The [`CIImage`](../../CoreImage/ciimage.md) instance.

## See Also

### Creating Representations of Core Image Objects
- [init(ciImage: CIImage)](./init%28ciimage%29-60ghw.md)
  Returns a representation of an image initialized to the specified Core Image instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsciimagerep/imagerepwithciimage:)*