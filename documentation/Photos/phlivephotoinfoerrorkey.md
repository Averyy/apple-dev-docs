# PHLivePhotoInfoErrorKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

An error that occurred while attempting to load the requested Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHLivePhotoInfoErrorKey: String
```

```c
extern NSString * const PHLivePhotoInfoErrorKey;
```

#### Discussion

The [`request(withResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:)`](./phlivephoto/request%28withresourcefileurls,placeholderimage,targetsize,contentmode,resulthandler%29.md) method validates that the files and their metadata can be loaded as a Live Photo. If Photos cannot load a Live Photo from the specified files, the `result` parameter in your result handler block is `nil`, and this key in the `info` dictionary contains an `NSError` object describing the error.

## See Also

### Constants
- [let PHLivePhotoInfoIsDegradedKey: String](./phlivephotoinfoisdegradedkey.md)
  A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.
- [let PHLivePhotoInfoCancelledKey: String](./phlivephotoinfocancelledkey.md)
  A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoinfoerrorkey)*