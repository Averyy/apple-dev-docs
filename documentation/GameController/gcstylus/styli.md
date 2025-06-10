# styli

**Framework**: Game Controller  
**Kind**: property

Get the collection of stylus accessories currently connected to the device.

**Availability**:
- visionOS ?+

## Declaration

```swift
class var styli: [GCStylus] { get }
```

## Mentions

- [Discovering and tracking spatial game controllers and styli](discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Discussion

This property returns an array of all currently connected stylus accessories. The array is empty when no stylus accessories are connected.  The array updates automatically as stylus accessories connect and disconnect.

To be notified when the array changes, register for the `GCStylusDidConnectNotification` and `GCStylusDidDisconnectNotification`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/styli)*