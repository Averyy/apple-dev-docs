# image

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns an image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var image: CGImage! { get }
```

```objc
@property (atomic, readonly) CGImageRef image;
```

## Return Value

An image.

## Discussion

Your data source must implement this method.

## See Also

### Getting Images From the Data Source
- [func thumbnail(withMaximumSize: NSSize) -> Unmanaged<CGImage>!](./thumbnail%28withmaximumsize%29.md)
  Returns a thumbnail image whose size is no larger than the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/image)*