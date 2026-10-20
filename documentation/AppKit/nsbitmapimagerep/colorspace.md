# colorSpace

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color space of the bitmap.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var colorSpace: NSColorSpace { get }
```

```objc
@property (strong, readonly) NSColorSpace * colorSpace;
```

## See Also

### Managing Color Spaces
- [func converting(to: NSColorSpace, renderingIntent: NSColorRenderingIntent) -> NSBitmapImageRep?](./converting%28to,renderingintent%29.md)
  Converts the bitmap image representation to the specified color space.
- [func retagging(with: NSColorSpace) -> NSBitmapImageRep?](./retagging%28with%29.md)
  Changes the color space tag of the bitmap image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/colorspace)*