# cancelLoadingImageData(forTag:)

**Framework**: Address Book  
**Kind**: method

Cancels an asynchronous fetch of the images for a given tag.

**Availability**:
- macOS ?+

## Declaration

```swift
class func cancelLoadingImageData(forTag tag: Int)
```

#### Discussion

The tag is returned from the previous call to the [`beginLoadingImageData(for:)`](abperson/beginloadingimagedata(for:).md) method that started the asynchronous fetch.

## Parameters

- `tag`: The tag of the asynchronous fetch to be canceled.

## See Also

- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](abperson/beginloadingimagedata(for:).md)
  Starts an asynchronous fetch for image data in all locations
- [func imageData() -> Data!](abperson/imagedata.md)
  Returns data that contains a picture of this person.
- [func setImageData(Data!) -> Bool](abperson/setimagedata(_:).md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/cancelloadingimagedata(fortag:))*