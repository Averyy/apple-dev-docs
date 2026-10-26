# init(ciImage:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a representation of an image initialized to the specified Core Image instance.

**Availability**:
- macOS

## Declaration

```swift
init(ciImage image: CIImage)
```

```objc
- (instancetype) initWithCIImage:(CIImage *) image;
```

#### Return Value

An initialized [`NSCIImageRep`](../nsciimagerep.md) object, or `nil` if the object could not be initialized.

## Parameters

- `image`: The [`CIImage`](../../CoreImage/ciimage.md) instance.

## See Also

### Creating Representations of Core Image Objects
- [+ imageRepWithCIImage:](./imagerepwithciimage_.md)
  Creates and returns a representation of an image initialized to the specified Core Image instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsciimagerep/init(ciimage:)-60ghw)*