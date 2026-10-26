# cancelRequest(withRequestID:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Cancels an asynchronous request

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func cancelRequest(withRequestID requestID: PHLivePhotoRequestID)
```

```objc
+ (void) cancelLivePhotoRequestWithRequestID:(PHLivePhotoRequestID) requestID;
```

#### Discussion

When you use the [`request(withResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:)`](./request%28withresourcefileurls,placeholderimage,targetsize,contentmode,resulthandler%29.md) method to asynchronously load a Live Photo from resource files, the method returns a numeric identifier for the request. To cancel the request before it completes, provide the identifier when calling the [`cancelRequest(withRequestID:)`](./cancelrequest%28withrequestid%29.md) method.

## Parameters

- `requestID`: The numeric identifier of the request to be canceled.

## See Also

### Loading a Live Photo from Data Files
- [class func request(withResourceFileURLs: [URL], placeholderImage: UIImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: (PHLivePhoto?, [AnyHashable : Any]) -> Void) -> PHLivePhotoRequestID](./request%28withresourcefileurls,placeholderimage,targetsize,contentmode,resulthandler%29.md)
  Asynchronously loads a Live Photo from the specified resource files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephoto/cancelrequest(withrequestid:))*