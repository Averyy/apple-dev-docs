# requestThumbnailImageURLForPreferredSize:resultHandler:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Returns a thumbnail using the provided \c PHPickerResultThumbnailSize.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```objc
- (void) requestThumbnailImageURLForPreferredSize:(PHPickerResultThumbnailSize) preferredSize resultHandler:(void (^)(NSURL *url, NSError *error)) resultHandler;
```

## Parameters

- `preferredSize`: A size recommendation for the thumbnail.
- `resultHandler`: Completion handler which returns the thumbnail URL and an error if there is one. The file at the URL is removed when the handler returns, so copy it to keep it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerresult-c.class/requestthumbnailimageurlforpreferredsize:resulthandler:)*