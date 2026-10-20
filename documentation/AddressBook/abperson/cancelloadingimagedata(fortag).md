# cancelLoadingImageData(forTag:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Type Method

Cancels an asynchronous fetch of the images for a given tag.

**Availability**:
- macOS

## Declaration

```swift
class func cancelLoadingImageData(forTag tag: Int)
```

```objc
+ (void) cancelLoadingImageDataForTag:(NSInteger) tag;
```

#### Discussion

The tag is returned from the previous call to the [`beginLoadingImageData(for:)`](./beginloadingimagedata%28for%29.md) method that started the asynchronous fetch.

## Parameters

- `tag`: The tag of the asynchronous fetch to be canceled.

## See Also

### Managing Images
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](./beginloadingimagedata%28for%29.md)
  Starts an asynchronous fetch for image data in all locations
- [func imageData() -> Data!](./imagedata%28%29.md)
  Returns data that contains a picture of this person.
- [func setImageData(Data!) -> Bool](./setimagedata%28_%29.md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/cancelloadingimagedata(fortag:))*