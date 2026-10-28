# PHLivePhotoInfoIsDegradedKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHLivePhotoInfoIsDegradedKey: String
```

```c
extern NSString * const PHLivePhotoInfoIsDegradedKey;
```

## Discussion

If `true`, the `result` parameter of your `resultHandler` block contains a still or low-quality Live Photo, and Photos will call your result handler block again to provide the full motion and sound content of the Live Photo. If `false`, Photos has provided all possible data and will not call your result handler again.

## See Also

### Constants
- [let PHLivePhotoInfoErrorKey: String](./phlivephotoinfoerrorkey.md)
  An error that occurred while attempting to load the requested Live Photo.
- [let PHLivePhotoInfoCancelledKey: String](./phlivephotoinfocancelledkey.md)
  A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoinfoisdegradedkey)*