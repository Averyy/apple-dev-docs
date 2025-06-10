# beginLoadingImageData(for:)

**Framework**: Address Book  
**Kind**: method

Starts an asynchronous fetch for image data in all locations

**Availability**:
- macOS ?+

## Declaration

```swift
func beginLoadingImageData(for client: (any ABImageClient)!) -> Int
```

#### Return Value

A nonzero tag for tracking. This tag is used by the [`cancelLoadingImageData(forTag:)`](abperson/cancelloadingimagedata(fortag:).md) method to cancel a fetch operation.

#### Discussion

The `client` object should conform to the `ABImageClient` protocol. A [`consumeImageData(_:forTag:)`](abimageclient/consumeimagedata(_:fortag:).md) message is sent to `client` when the fetch is done. Use the [`cancelLoadingImageData(forTag:)`](abperson/cancelloadingimagedata(fortag:).md) method if you need to cancel an asynchronous fetch.

## Parameters

- `client`: The object to be notified when the image finishes loading.

## See Also

- [class func cancelLoadingImageData(forTag: Int)](abperson/cancelloadingimagedata(fortag:).md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func imageData() -> Data!](abperson/imagedata.md)
  Returns data that contains a picture of this person.
- [func setImageData(Data!) -> Bool](abperson/setimagedata(_:).md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/beginloadingimagedata(for:))*