# invalidationHandler(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles session invalidation.

**Availability**:
- iOS 26.2+ - Deprecated in 26.5 (renamed: sessionInvalidated(error:))

## Declaration

```swift
func invalidationHandler(error: AccessoryTransportSession.Error?)
```

## Parameters

- `error`: An optional error that indicates the reason for cancellation.

## Default Implementations

### AccessoryTransportSession.EventHandler Implementations
- [func invalidationHandler(error: AccessoryTransportSession.Error?)](./invalidationhandler%28error%29-3t0i7.md)
  Session has been invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/invalidationhandler(error:))*