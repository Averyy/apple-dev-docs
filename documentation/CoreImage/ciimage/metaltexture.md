# metalTexture

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var metalTexture: (any MTLTexture)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLTexture> metalTexture;
```

## See Also

### Instance Properties
- [var contentHeadroom: Float](./contentheadroom.md)
  Returns the content headroom of the image.
- [var isOpaque: Bool](./isopaque.md)
  Returns YES if the image is known to have and alpha value of `1.0` over the entire image extent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/metaltexture)*