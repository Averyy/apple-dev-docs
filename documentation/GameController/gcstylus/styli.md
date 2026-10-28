# styli

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

Get the collection of stylus accessories currently connected to the device.

**Availability**:
- visionOS

## Declaration

```swift
class var styli: [GCStylus] { get }
```

```objc
@property (class, readonly) NSArray<GCStylus *> * styli;
```

## Mentions

- [Discovering and tracking spatial game controllers and styli](../discovering-and-tracking-spatial-game-controllers-and-styli.md)

## Discussion

This property returns an array of all currently connected stylus accessories. The array is empty when no stylus accessories are connected.  The array updates automatically as stylus accessories connect and disconnect.

To be notified when the array changes, register for the `GCStylusDidConnectNotification` and `GCStylusDidDisconnectNotification`.

## See Also

### Accessing the styli
- [GCStylusDidConnectNotification](../gcstylusdidconnectnotification.md)
  A notification that posts after a stylus accessory connects to the device.
- [GCStylusDidDisconnectNotification](../gcstylusdiddisconnectnotification.md)
  A notification that posts after a stylus accessory disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/styli)*