# sessionStarted(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the handler when its feature session starts.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func sessionStarted(_ session: Self.Session)
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Discussion

Save this session so your app can send data to the transport extension at a later time.

## Parameters

- `session`: The session that starts. Hold this parameter with a weak reference because the system owns it.

## See Also

### Handling the session life cycle
- [func sessionInvalidated(error: (any Error)?)](./sessioninvalidated%28error%29.md)
  Notifies the handler when its feature session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesessionhandler/sessionstarted(_:))*