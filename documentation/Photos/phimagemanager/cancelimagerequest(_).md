# cancelImageRequest(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Cancels an asynchronous request

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancelImageRequest(_ requestID: PHImageRequestID)
```

```objc
- (void) cancelImageRequest:(PHImageRequestID) requestID;
```

#### Discussion

When you perform an asynchronous request for image data using the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](./requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method, or for a video object using one of the methods listed in Requesting Video Objects, the image manager returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

## Parameters

- `requestID`: The numeric identifier of the request to be canceled.

## See Also

### Canceling a Request
- [typealias PHImageRequestID](../phimagerequestid.md)
  A numeric identifier for an asynchronous image request.
- [var PHInvalidImageRequestID: PHImageRequestID](../phinvalidimagerequestid.md)
  A special value provided for asynchronous image requests that cannot be canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/cancelimagerequest(_:))*