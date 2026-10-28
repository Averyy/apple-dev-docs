# stopBrowsingForNearbyPlayers()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Stops finding nearby players.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stopBrowsingForNearbyPlayers()
```

```objc
- (void) stopBrowsingForNearbyPlayers;
```

## Discussion

If you use the [`startBrowsingForNearbyPlayers(handler:)`](./startbrowsingfornearbyplayers%28handler%29.md) method to find nearby players, call this method when you are done.

## See Also

### Looking for nearby players
- [func startBrowsingForNearbyPlayers(handler: ((GKPlayer, Bool) -> Void)?)](./startbrowsingfornearbyplayers%28handler%29.md)
  Finds nearby players through Bluetooth or WiFi on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/stopbrowsingfornearbyplayers())*