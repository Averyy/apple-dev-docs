# setImageData(_:)

**Framework**: Address Book  
**Kind**: method

Sets the image for this person to the given data.

**Availability**:
- macOS ?+

## Declaration

```swift
func setImageData(_ data: Data!) -> Bool
```

#### Discussion

The `data` argument must be in a QuickTime-compatible format. Pass `nil` to specify that there is no image for this person.

## Parameters

- `data`: The image to be set.

## See Also

- [class func cancelLoadingImageData(forTag: Int)](abperson/cancelloadingimagedata(fortag:).md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](abperson/beginloadingimagedata(for:).md)
  Starts an asynchronous fetch for image data in all locations
- [func imageData() -> Data!](abperson/imagedata.md)
  Returns data that contains a picture of this person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/setimagedata(_:))*