# PHLivePhotoInfoCancelledKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHLivePhotoInfoCancelledKey: String
```

```c
extern NSString * const PHLivePhotoInfoCancelledKey;
```

#### Discussion

If you call the [`cancelRequest(withRequestID:)`](./phlivephoto/cancelrequest%28withrequestid%29.md) method to cancel a request, Photos calls your result handler block with a `true` value for this key.

## See Also

### Constants
- [let PHLivePhotoInfoErrorKey: String](./phlivephotoinfoerrorkey.md)
  An error that occurred while attempting to load the requested Live Photo.
- [let PHLivePhotoInfoIsDegradedKey: String](./phlivephotoinfoisdegradedkey.md)
  A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoinfocancelledkey)*