# requestData(for:options:dataReceivedHandler:completionHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests the underlying data for the specified asset resource, to be delivered asynchronously.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestData(for resource: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler handler: @escaping (Data) -> Void, completionHandler: @escaping ((any Error)?) -> Void) -> PHAssetResourceDataRequestID
```

```objc
- (PHAssetResourceDataRequestID) requestDataForAssetResource:(PHAssetResource *) resource options:(PHAssetResourceRequestOptions *) options dataReceivedHandler:(void (^)(NSData *data)) handler completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelDataRequest(_:)`](./canceldatarequest%28_%29.md) method.

#### Discussion

When you call this method, Photos begins asynchronously reading the underlying data for the asset resource. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

While reading (or downloading) asset resource data, Photos calls your `handler` block at least once, progressively providing chunks of data. After reading all of the data, Photos calls your `completionHandler` block to indicate that the data is complete. (At this point, the complete data for the asset is the concatenation of the `data` parameters from all calls to your `handler` block.) If Photos cannot finish reading or downloading asset resource data, it calls your `completionHandler` block with a description of the error. Photos can also call the `completionHandler` block with a non-nil error when the data is complete if the user cancels downloading.

> **Note**:  Photos calls your `handler` and `completionHandler` blocks on an arbitrary serial queue. To update the UI in response to these events, dispatch to the main queue.

## Parameters

- `resource`: The asset resource for which to request data.
- `options`: Options specifying how Photos should handle the request and notify your app of progress. For details, see [`PHAssetResourceRequestOptions`](../phassetresourcerequestoptions.md).
- `handler`: A block that Photos calls to provide the requested data.

  The block takes a single parameter:

  - **data**: The requested asset resource data.
- `completionHandler`: A block that photos calls after the request has been fulfilled or has failed.

  The block takes a single parameter:

  - **error**: If the request has failed, an `NSError` object describing the failure; otherwise `nil`.

## See Also

### Requesting Resources
- [func cancelDataRequest(PHAssetResourceDataRequestID)](./canceldatarequest%28_%29.md)
  Cancels an asynchronous request.
- [func writeData(for: PHAssetResource, toFile: URL, options: PHAssetResourceRequestOptions?, completionHandler: ((any Error)?) -> Void)](./writedata%28for,tofile,options,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager/requestdata(for:options:datareceivedhandler:completionhandler:))*