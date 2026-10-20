# outputWidth

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

The width of the output color texture for the temporal scaler you create with this descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+

## Declaration

```swift
var outputWidth: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger outputWidth;
```

## See Also

### Configuring a temporal effect’s output
- [var outputHeight: Int](./outputheight.md)
  The height of the output color texture for the temporal scaler you create with this descriptor.
- [var outputTextureFormat: MTLPixelFormat](./outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/outputwidth)*