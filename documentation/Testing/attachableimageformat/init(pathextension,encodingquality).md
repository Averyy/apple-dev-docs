# init(pathExtension:encodingQuality:)

**Framework**: Swift Testing  
**Kind**: init

Construct an instance of this type with the given path extension and encoding quality.

**Availability**:
- Swift 6.3+
- Xcode 26.4+

## Declaration

```swift
init?(pathExtension: String, encodingQuality: Float = 1.0)
```

#### Discussion

If the target image format does not support variable-quality encoding, the value of the `encodingQuality` argument is ignored.

If `pathExtension` does not correspond to a recognized image format, this initializer returns `nil`:

- On Apple platforms, the content type corresponding to `pathExtension` must conform to [`UTType.image`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/image).
- On Windows, there must be a corresponding subclass of [`IWICBitmapEncoder`](https://developer.apple.comhttps://learn.microsoft.com/en-us/windows/win32/api/wincodec/nn-wincodec-iwicbitmapencoder) registered with Windows Imaging Component.

## Parameters

- `pathExtension`: A path extension corresponding to the image format to use when encoding images.
- `encodingQuality`: The encoding quality to use when encoding images. For the lowest supported quality, pass `0.0`. For the highest supported quality, pass `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableimageformat/init(pathextension:encodingquality:))*