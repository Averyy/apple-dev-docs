# removeSession:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Removes a session from the active route.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) removeSession:(AVSystemRouteSession *) session;
```

#### Discussion

Call this method to unregister a session from the route when playback ends or when you no longer need the session. Removing a session stops any ongoing communication associated with that session and releases system resources.

If the session is currently active, this method stops the session before removing it.

> ❗ **Important**: Always remove sessions when they are no longer needed to ensure proper cleanup of system resources and network connections. To start new playback after removing a session, create a new [`AVSystemRouteSession`](../avsystemroutesession-5i6j6.md) instance.

## Parameters

- `session`: The session to remove from this route. If the session is not currently associated with this route, this method has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-9kkj3/removesession:)*