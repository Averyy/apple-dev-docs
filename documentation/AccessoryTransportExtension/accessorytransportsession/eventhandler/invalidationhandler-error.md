# invalidationHandler(error:)

**Framework**: AccessoryTransportExtension  
**Kind**: method  
**Required**: Yes

Handles cancellation of the session, in response to a call from the framework.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
func invalidationHandler(error: AccessoryTransportSession.Error?)
```

## Parameters

- `error`: The error that caused the session cancellation.

## See Also

- [AccessoryTransportSession.Error](accessorytransportsession/error.md)
  A type that defines errors encountered when using an accessory transport session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/invalidationhandler(error:))*