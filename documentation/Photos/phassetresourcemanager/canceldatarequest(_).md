# cancelDataRequest(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Cancels an asynchronous request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancelDataRequest(_ requestID: PHAssetResourceDataRequestID)
```

```objc
- (void) cancelDataRequest:(PHAssetResourceDataRequestID) requestID;
```

## Discussion

When you perform an asynchronous request for asset resource data using the [`requestData(for:options:dataReceivedHandler:completionHandler:)`](./requestdata%28for,options,datareceivedhandler,completionhandler%29.md) method, the image manager returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [`cancelDataRequest(_:)`](./canceldatarequest%28_%29.md) method.

## Parameters

- `requestID`: The numeric identifier of the request to be canceled.

## See Also

### Requesting Resources
- [func requestData(for: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler: (Data) -> Void, completionHandler: ((any Error)?) -> Void) -> PHAssetResourceDataRequestID](./requestdata%28for,options,datareceivedhandler,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [func writeData(for: PHAssetResource, toFile: URL, options: PHAssetResourceRequestOptions?, completionHandler: ((any Error)?) -> Void)](./writedata%28for,tofile,options,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager/canceldatarequest(_:))*