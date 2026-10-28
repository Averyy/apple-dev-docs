# PHImageRequestID

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

A numeric identifier for an asynchronous image request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHImageRequestID = Int32
```

```c
typedef int32_t PHImageRequestID;
```

## Discussion

Pass this identifier to the [`cancelImageRequest(_:)`](./phimagemanager/cancelimagerequest%28_%29.md) method if you need to cancel a request before it completes.

## See Also

### Canceling a Request
- [func cancelImageRequest(PHImageRequestID)](./phimagemanager/cancelimagerequest%28_%29.md)
  Cancels an asynchronous request
- [var PHInvalidImageRequestID: PHImageRequestID](./phinvalidimagerequestid.md)
  A special value provided for asynchronous image requests that cannot be canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestid)*