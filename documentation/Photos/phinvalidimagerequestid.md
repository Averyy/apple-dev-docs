# PHInvalidImageRequestID

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A special value provided for asynchronous image requests that cannot be canceled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var PHInvalidImageRequestID: PHImageRequestID { get }
```

```c
static const PHImageRequestID PHInvalidImageRequestID;
```

## See Also

### Canceling a Request
- [func cancelImageRequest(PHImageRequestID)](./phimagemanager/cancelimagerequest%28_%29.md)
  Cancels an asynchronous request
- [typealias PHImageRequestID](./phimagerequestid.md)
  A numeric identifier for an asynchronous image request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phinvalidimagerequestid)*