# requestThumbnailImageURL(preferredSize:resultHandler:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Returns a thumbnail using the provided `PHPickerResultThumbnailSize`.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
func requestThumbnailImageURL(preferredSize: PHPickerResultThumbnailSize, resultHandler: @escaping (Result<URL, any Error>) -> Void)
```

## Parameters

- `preferredSize`: A size recommendation for the thumbnail.
- `resultHandler`: Completion handler which returns the thumbnail URL or an error. The file at the URL is removed when the handler returns, so copy it to keep it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerresult-swift.struct/requestthumbnailimageurl(preferredsize:resulthandler:))*