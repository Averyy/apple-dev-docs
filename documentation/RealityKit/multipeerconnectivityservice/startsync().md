# startSync()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Begins multipeer synchronization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func startSync()
```

## Discussion

Call this method to restart multipeer syncing with connected peers after calling [`stopSync()`](./stopsync%28%29.md). You don’t need to call this method to begin syncing. RealityKit calls this method automatically when you assign a [`MultipeerConnectivityService`](../multipeerconnectivityservice.md) to a [`Scene`](../scene.md).

## See Also

### Pausing and resuming
- [func stopSync()](./stopsync%28%29.md)
  Stops multipeer synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/multipeerconnectivityservice/startsync())*