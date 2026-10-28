# addSession:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Adds a session to the active route.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (BOOL) addSession:(AVSystemRouteSession *) session;
```

## Return Value

`true` if the route successfully adds the session; `false` if the route cannot add it (for example, if the session is already associated with another route or if the route is in an invalid state).

## Discussion

Call this method to register a new [`AVSystemRouteSession`](../avsystemroutesession-5i6j6.md) with the route before starting playback or communication. The session must be added to the route before calling its [`startWithCompletionHandler:`](../avsystemroutesession-5i6j6/startwithcompletionhandler_.md) method.

Adding a session establishes the association between the session and this route, enabling the system to manage the session’s lifecycle and route media appropriately. You can add multiple sessions to a single route to handle different media streams or communication channels.

Sessions are single-use. Once a session has been stopped, it cannot be added to a route again. Create a new [`AVSystemRouteSession`](../avsystemroutesession-5i6j6.md) for each new playback.

> **Note**: You must remove sessions when they are no longer needed using [`removeSession:`](./removesession_.md) to release system resources.

## Parameters

- `session`: The session to add to this route. The session must be newly created and not already associated with another route or previously stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-9kkj3/addsession:)*