# sendChangesWithCompletionHandler:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Sends pending local changes to the server.

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
- (void) sendChangesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

If the send fails, the completion handler’s `error` parameter is an object that describes that failure; otherwise, it’s `nil`.

Use this method to request the sync engine sends all pending local changes to the server before your app continues. This isn’t necessary in normal use, as the engine automatically syncs your app’s records. It is useful, however, in scenarios where you require greater control over sync, such as a “Backup now” button or unit tests.

> **Note**: The sync engine invokes the completion handler only after your sync delegate finishes processing all related send events.

## Parameters

- `completionHandler`: The block to execute when the send completes.

## See Also

### Invoking manual sync operations
- [- fetchChangesWithCompletionHandler:](./fetchchangeswithcompletionhandler_.md)
  Fetches pending remote changes from the server.
- [- fetchChangesWithOptions:completionHandler:](./fetchchangeswithoptions_completionhandler_.md)
  Fetches pending remote changes from the server using the specified options.
- [CKSyncEngineFetchChangesOptions](../cksyncenginefetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [- sendChangesWithOptions:completionHandler:](./sendchangeswithoptions_completionhandler_.md)
  Sends pending local changes to the server using the specified options.
- [CKSyncEngineSendChangesOptions](../cksyncenginesendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9/sendchangeswithcompletionhandler:)*