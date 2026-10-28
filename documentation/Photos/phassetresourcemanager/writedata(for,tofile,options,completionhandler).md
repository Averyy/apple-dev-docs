# writeData(for:toFile:options:completionHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func writeData(for resource: PHAssetResource, toFile fileURL: URL, options: PHAssetResourceRequestOptions?, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeData(for resource: PHAssetResource, toFile fileURL: URL, options: PHAssetResourceRequestOptions?) async throws
```

```objc
- (void) writeDataForAssetResource:(PHAssetResource *) resource toFile:(NSURL *) fileURL options:(PHAssetResourceRequestOptions *) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

When you call this method, Photos begins asynchronously reading the underlying data for the asset resource. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

While reading (or downloading) asset resource data, Photos progressively writes the data into the specified file. After writing all of the data, or if an error prevents reading all of the data, Photos calls your `completionHandler` block.

> **Note**:  Photos calls your `completionHandler` block on an arbitrary serial queue. To update the UI in response to these events, dispatch to the main queue.

## Parameters

- `resource`: The asset resource for which to request data.
- `fileURL`: A URL identifying the local filename at which to write the asset resource’s data.
- `options`: Options specifying how Photos should handle the request and notify your app of progress. For details, see [`PHAssetResourceRequestOptions`](../phassetresourcerequestoptions.md).
- `completionHandler`: A block that photos calls after the request has been fulfilled or has failed.

  The block takes a single parameter:

  - **error**: If the request has failed, an `NSError` object describing the failure; otherwise `nil`.

## See Also

### Requesting Resources
- [func requestData(for: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler: (Data) -> Void, completionHandler: ((any Error)?) -> Void) -> PHAssetResourceDataRequestID](./requestdata%28for,options,datareceivedhandler,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [func cancelDataRequest(PHAssetResourceDataRequestID)](./canceldatarequest%28_%29.md)
  Cancels an asynchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager/writedata(for:tofile:options:completionhandler:))*