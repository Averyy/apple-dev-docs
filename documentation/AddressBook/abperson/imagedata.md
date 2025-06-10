# imageData()

**Framework**: Address Book  
**Kind**: method

Returns data that contains a picture of this person.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageData() -> Data!
```

#### Return Value

Data containing a picture of this person

#### Discussion

This method searches only the local file system and operates synchronously. To perform an asynchronous search or to search over a network, use [`beginLoadingImageData(for:)`](abperson/beginloadingimagedata(for:).md).

The returned data is in a QuickTime-compatible format. To create an image from it, use the `NSImage` method [`init(data:)`](https://developer.apple.com/documentation/AppKit/NSImage/init(data:)).

## See Also

- [class func cancelLoadingImageData(forTag: Int)](abperson/cancelloadingimagedata(fortag:).md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](abperson/beginloadingimagedata(for:).md)
  Starts an asynchronous fetch for image data in all locations
- [func setImageData(Data!) -> Bool](abperson/setimagedata(_:).md)
  Sets the image for this person to the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/imagedata())*