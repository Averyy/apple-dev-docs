# cgImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Core Graphics image object based on the bitmap image representation’s data.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var cgImage: CGImage? { get }
```

```objc
@property (readonly, nullable) CGImageRef CGImage;
```

#### Discussion

The autoreleased [`CGImage`](../../CoreGraphics/cgimage.md) opaque type in this property has pixel dimensions that are identical to those of the bitmap image rep object. If an existing [`CGImage`](../../CoreGraphics/cgimage.md) opaque type is not available, accessing this property creates a new one. If you change the bitmap image rep’s contents later, accessing this property again might return a different [`CGImage`](../../CoreGraphics/cgimage.md) opaque type.

## See Also

### Related Documentation
- [init(cgImage: CGImage)](./init%28cgimage%29-7o5tz.md)
  Returns a bitmap image representation from a Core Graphics image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/cgimage)*