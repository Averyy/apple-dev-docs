# thumbnail(withMaximumSize:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns a thumbnail image whose size is no larger than the specified size.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func thumbnail(withMaximumSize size: NSSize) -> Unmanaged<CGImage>!
```

```objc
- (CGImageRef) thumbnailWithMaximumSize:(NSSize) size;
```

#### Return Value

An image.

## See Also

### Getting Images From the Data Source
- [var image: CGImage!](./image.md)
  Returns an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/thumbnail(withmaximumsize:))*