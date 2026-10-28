# imageData()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns data that contains a picture of this person.

**Availability**:
- macOS

## Declaration

```swift
func imageData() -> Data!
```

```objc
- (NSData *) imageData;
```

## Return Value

Data containing a picture of this person

## Discussion

This method searches only the local file system and operates synchronously. To perform an asynchronous search or to search over a network, use [`beginLoadingImageData(for:)`](./beginloadingimagedata%28for%29.md).

The returned data is in a QuickTime-compatible format. To create an image from it, use the `NSImage` method [`init(data:)`](../../AppKit/nsimage/init%28data%29.md).

## See Also

### Managing Images
- [class func cancelLoadingImageData(forTag: Int)](./cancelloadingimagedata%28fortag%29.md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](./beginloadingimagedata%28for%29.md)
  Starts an asynchronous fetch for image data in all locations
- [func setImageData(Data!) -> Bool](./setimagedata%28_%29.md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/imagedata())*