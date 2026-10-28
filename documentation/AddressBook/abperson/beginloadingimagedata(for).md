# beginLoadingImageData(for:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Starts an asynchronous fetch for image data in all locations

**Availability**:
- macOS

## Declaration

```swift
func beginLoadingImageData(for client: (any ABImageClient)!) -> Int
```

```objc
- (NSInteger) beginLoadingImageDataForClient:(id<ABImageClient>) client;
```

## Return Value

A nonzero tag for tracking. This tag is used by the [`cancelLoadingImageData(forTag:)`](./cancelloadingimagedata%28fortag%29.md) method to cancel a fetch operation.

## Discussion

The `client` object should conform to the `ABImageClient` protocol. A [`consumeImageData(_:forTag:)`](../abimageclient/consumeimagedata%28_,fortag%29.md) message is sent to `client` when the fetch is done. Use the [`cancelLoadingImageData(forTag:)`](./cancelloadingimagedata%28fortag%29.md) method if you need to cancel an asynchronous fetch.

## Parameters

- `client`: The object to be notified when the image finishes loading.

## See Also

### Managing Images
- [class func cancelLoadingImageData(forTag: Int)](./cancelloadingimagedata%28fortag%29.md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func imageData() -> Data!](./imagedata%28%29.md)
  Returns data that contains a picture of this person.
- [func setImageData(Data!) -> Bool](./setimagedata%28_%29.md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/beginloadingimagedata(for:))*