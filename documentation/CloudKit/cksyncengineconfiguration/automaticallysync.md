# automaticallySync

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the engine syncs automatically.

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
@property (assign) BOOL automaticallySync;
```

## Discussion

By default, the sync engine uses the system scheduler to automatically schedule both send and fetch operations. If an operation fails due to a recoverable error, such as a network failure, or when the server is enforcing request limits, the engine reschedules those operations as necessary. Unless you have a specific need, prefer to use the default behavior in your app.

If you set this property’s value to [`false`](../../Swift/false.md), use [`fetchChangesWithCompletionHandler:`](../cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md) and [`sendChangesWithCompletionHandler:`](../cksyncengine-4b4w9/sendchangeswithcompletionhandler_.md) to invoke immediate sync operations, allowing for more control over when your app syncs its records. For example, you may want to sync at a specific time of day, or deterministically simulate certain conditions in your unit tests.

The default value is [`true`](../../Swift/true.md).

## See Also

### Managing attributes
- [database](./database.md)
  The associated database.
- [subscriptionID](./subscriptionid.md)
  The subscription identifier for the associated database.
- [stateSerialization](./stateserialization.md)
  The sync engine’s serialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineconfiguration/automaticallysync)*