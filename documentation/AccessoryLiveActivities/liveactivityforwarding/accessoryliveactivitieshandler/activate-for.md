# activate(for:)

**Framework**: Accessory Live Activities  
**Kind**: method  
**Required**: Yes

Establishes communication between the data provider extension and the system.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func activate(for session: LiveActivityForwarding.Session)
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Store a reference to the session and use it to receive life-cycle events and updates to ongoing Live Activities. The session becomes invalid after the system calls [`sessionInvalidated()`](liveactivityforwarding/accessoryliveactivitieshandler/sessioninvalidated().md) to indicate that the system won’t deliver Live Activities to your accessory. Don’t use the session after invalidation.

## Parameters

- `session`: A session object that enables communication between your accessory’s data provider extension and the system.

## See Also

- [func sessionInvalidated()](liveactivityforwarding/accessoryliveactivitieshandler/sessioninvalidated.md)
  Indicates that the system invalidated the session and stopped sending Live Activity updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler/activate(for:))*