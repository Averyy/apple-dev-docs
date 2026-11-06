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

The system calls this method once the session activates and your app enrolls the feature.

## Parameters

- `session`: The session that starts. Hold a weak reference to this parameter because the [`makeFeatureSession(_:)`](../accessorytransportsession/makefeaturesession%28_%29.md) caller owns it.

## See Also

### Handling the session life cycle
- [func sessionInvalidated(error: (any Error)?)](./sessioninvalidated%28error%29.md)
  Notifies the handler when its feature session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesessionhandler/sessionstarted(_:))*