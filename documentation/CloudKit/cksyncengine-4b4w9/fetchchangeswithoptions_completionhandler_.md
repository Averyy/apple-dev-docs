# fetchChangesWithOptions:completionHandler:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches pending remote changes from the server using the specified options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (void) fetchChangesWithOptions:(CKSyncEngineFetchChangesOptions *) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

If the fetch fails, the completion handler’s `error` parameter is an object that describes that failure; otherwise, it’s `nil`.

Use this method to request the sync engine immediately fetches all pending remote changes before your app continues. This isn’t necessary in normal use, as the engine automatically syncs your app’s records. It is useful, however, in scenarios where you require more control over sync, such as pull-to-refresh or unit tests.

> **Note**: The sync engine invokes the completion handler only after your sync delegate finishes processing all related fetch events.

## Parameters

- `options`: The options to use when fetching changes. For more information, see [`CKSyncEngineFetchChangesOptions`](../cksyncenginefetchchangesoptions.md).
- `completionHandler`: The block to execute when the fetch completes.

## See Also

### Invoking manual sync operations
- [- fetchChangesWithCompletionHandler:](./fetchchangeswithcompletionhandler_.md)
  Fetches pending remote changes from the server.
- [CKSyncEngineFetchChangesOptions](../cksyncenginefetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [- sendChangesWithCompletionHandler:](./sendchangeswithcompletionhandler_.md)
  Sends pending local changes to the server.
- [- sendChangesWithOptions:completionHandler:](./sendchangeswithoptions_completionhandler_.md)
  Sends pending local changes to the server using the specified options.
- [CKSyncEngineSendChangesOptions](../cksyncenginesendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9/fetchchangeswithoptions:completionhandler:)*