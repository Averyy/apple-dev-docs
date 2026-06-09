# addSession(_:)

**Framework**: AVSystemRouting  
**Kind**: method

Adds a session to the active route.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func addSession(_ session: AVSystemRouteSession) -> Bool
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Return Value

`true` if the route successfully adds the session; `false` if the route cannot add it (for example, if the session is already associated with another route or if the route is in an invalid state).

#### Discussion

Call this function to register a new [`AVSystemRouteSession`](avsystemroutesession-gp78.md) with the route before starting playback or communication. The session must be added to the route before calling its [`start()`](avsystemroutesession-gp78/start().md) function.

Adding a session establishes the association between the session and this route, enabling the system to manage the session’s lifecycle and route media appropriately. You can add multiple sessions to a single route to handle different media streams or communication channels.

Sessions are single-use. Once a session has been stopped, it cannot be added to a route again. Create a new [`AVSystemRouteSession`](avsystemroutesession-gp78.md) for each new playback.

> **Note**: You must remove sessions when they are no longer needed using [`removeSession(_:)`](avsystemroute-5s2um/removesession(_:).md) to release system resources.

## Parameters

- `session`: The session to add to this route. The session must be newly created and not already associated with another route or previously stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/addsession(_:))*