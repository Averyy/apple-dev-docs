# PHLivePhotoRequestID

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

A numeric identifier for an asynchronous Live Photo loading request.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHLivePhotoRequestID = Int32
```

```c
typedef int32_t PHLivePhotoRequestID;
```

## Discussion

Pass this identifier to the [`cancelRequest(withRequestID:)`](./phlivephoto/cancelrequest%28withrequestid%29.md) method if you need to cancel a request before it completes.

## See Also

### Constants
- [Image Request Identifiers](../PhotoKit/image-request-identifiers.md)
  Special values for the Live Photo request ID that are returned by asynchronous requests.
- [Result Handler Info Dictionary Keys](../PhotoKit/result-handler-info-dictionary-keys.md)
  Info describing an attempt to load a Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestid)*