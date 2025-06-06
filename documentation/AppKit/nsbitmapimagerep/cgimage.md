# cgImage

**Framework**: AppKit  
**Kind**: property

A Core Graphics image object based on the bitmap image representation’s data.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var cgImage: CGImage? { get }
```

#### Discussion

The autoreleased [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) opaque type in this property has pixel dimensions that are identical to those of the bitmap image rep object. If an existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) opaque type is not available, accessing this property creates a new one. If you change the bitmap image rep’s contents later, accessing this property again might return a different [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) opaque type.

## See Also

- [init(cgImage: CGImage)](nsbitmapimagerep/init(cgimage:).md)
  Returns a bitmap image representation from a Core Graphics image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/cgimage)*