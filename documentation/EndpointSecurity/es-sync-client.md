# es_sync_client(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_sync_client(_ client: OpaquePointer, _ block: @escaping () -> Void) -> es_return_t
```

#### Discussion

Place a sync marker at the back of the message queue for `client`, run `block` when it reaches the front of the queue.

To best take advantage of this function it’s important the caller understand the message queue invariants of an ES client.

When a program issues a syscall (or similar), it is guaranteed that before control is returned to the caller, the associated ES message has been created and enqueued with all ES clients. Message delivery is asynchronous (even for auth evnts), but enqueing is fully synchronous. With that in mind, it makes it possible to write such code as:

```None
dispatch_semaphore_t sema = dispatch_semaphore_create(0);
(void)open("/tmp/foo");
es_sync_client(client, ^(){ dispatch_semaphore_signal(sema); });
dispatch_semaphore_wait(sema, DISPATCH_TIME_FOREVER);
// At this point the open event for /tmp/foo has been delivered
```

This is useful for any program that both has effects and subsribes to ES events. `es_sync_client()` can tell you “When have all the events I am waiting for arrived?”

Sync points are a more general concept with uses beyond this, for example if a caller unsubscribes from a certain event type, they could then call `es_sync_client()`, and after the callback fires, know that all events of that type have now been delivered.

> **Note**: If the ES client is destroyed, all sync blocks are called.

> **Note**: This forces the current batch of messages to be flushed, the handler will be scheduled until the sync marker is reached.

> **Note**: Can NOT be called from the ES handler block of `client`.

> **Note**: If client is null, the callback is immediately invoked and the function returns `ES_RETURN_SUCCESS`.

## Parameters

- `client`: The client to synchronise.
- `block`: The block that runs after all messages in front of the sync marker have been handled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_sync_client(_:_:))*