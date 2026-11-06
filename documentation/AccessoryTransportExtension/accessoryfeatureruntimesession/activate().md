# activate()

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Registers the session and requests that the system start it.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func activate() async throws
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Discussion

Returning from this method doesn’t mean the session started. The system calls [`sessionStarted(_:)`](../accessoryfeatureruntimesessionhandler/sessionstarted%28_%29.md) after registering the session and after your app enrolls the feature. For more information about feature enrollment, see [Accessory features](../accessory-features.md).

This method throws [`AccessoryTransportSession.Error.unavailable`](../accessorytransportsession/error/unavailable.md) if the feature isn’t available on the device, and the system throws an error if a live session for the same feature already exists.

This method doesn’t throw when the feature isn’t enrolled for the accessory. Check the status with `AccessoryWorker/authorizationStatus(for:)` before you call this method.

## Default Implementations

### AccessoryFeatureRuntimeSession Implementations
- [func activate() async throws](./activate%28%29-6fbg3.md)

## See Also

### Managing the session life cycle
- [func invalidate()](./invalidate%28%29.md)
  Unregisters the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesession/activate())*