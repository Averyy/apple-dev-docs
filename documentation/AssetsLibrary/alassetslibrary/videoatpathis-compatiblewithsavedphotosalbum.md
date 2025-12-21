# videoAtPathIs(compatibleWithSavedPhotosAlbum:)

**Framework**: Assets Library  
**Kind**: method

Returns a Boolean value that indicates whether a video identified by a given URL is compatible with the Saved Photos album.

## Declaration

```swift
func videoAtPathIs(compatibleWithSavedPhotosAlbum videoPathURL: URL!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the video identified by `videoPathURL` is compatible with the Saved Photos album, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns the same value as [`UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_:)`](https://developer.apple.com/documentation/UIKit/UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_:)) would for the same URL.

## Parameters

- `videoPathURL`: An URL that points to a video file.

## See Also

- [func writeVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves a video identified by a given URL to the Saved Photos album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, orientation: ALAssetOrientation, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md)
  Saves a given image to the Saved Photos album.
- [func writeImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Writes given image data and metadata to the Photos Album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:metadata:completionblock:).md)
  Writes a given image and metadata to the Photos Album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/videoatpathis(compatiblewithsavedphotosalbum:))*