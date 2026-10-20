# setImageData(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Sets the image for this person to the given data.

**Availability**:
- macOS

## Declaration

```swift
func setImageData(_ data: Data!) -> Bool
```

```objc
- (BOOL) setImageData:(NSData *) data;
```

#### Discussion

The `data` argument must be in a QuickTime-compatible format. Pass `nil` to specify that there is no image for this person.

## Parameters

- `data`: The image to be set.

## See Also

### Managing Images
- [class func cancelLoadingImageData(forTag: Int)](./cancelloadingimagedata%28fortag%29.md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](./beginloadingimagedata%28for%29.md)
  Starts an asynchronous fetch for image data in all locations
- [func imageData() -> Data!](./imagedata%28%29.md)
  Returns data that contains a picture of this person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/setimagedata(_:))*