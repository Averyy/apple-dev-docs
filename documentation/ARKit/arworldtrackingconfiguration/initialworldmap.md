# initialWorldMap

**Framework**: ARKit  
**Kind**: property

The state from a previous AR session to attempt to resume with this session configuration.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var initialWorldMap: ARWorldMap? { get set }
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

An [`ARWorldMap`](arworldmap.md) encapsulates the state of a running [`ARSession`](arsession.md). This state includes ARKit’s awareness of the physical space the user moves the device in (which ARKit uses to determine the device’s position and orientation), as well as any [`ARAnchor`](aranchor.md) objects added to the session (which can represent detected real-world features or virtual content placed by your app). After you use  [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md) to save a session’s world map, you can assign it to a configuration’s [`initialWorldMap`](arworldtrackingconfiguration/initialworldmap.md) property and use [`run(_:options:)`](arsession/run(_:options:).md) to start another session with the same spatial awareness and anchors.

By saving world maps and using them to start new sessions, your app can add new AR capabilities:

-  Create a shared frame of reference by sending archived [`ARWorldMap`](arworldmap.md) objects to a nearby user’s device. With two devices tracking the same world map, you can build a networked experience where both users can see and interact with the same virtual content.
-  Save a world map when your app becomes inactive, then restore it the next time your app launches in the same physical environment. You can use  anchors from the resumed world map to place the same virtual content at the same positions from the saved session.

When you run a session with an initial world map, the session starts in the [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md) ([`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md)) tracking state while ARKit attempts to reconcile the recorded world map with the current environment. If successful, the tracking state becomes [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md) after a short time, indicating that the current world coordinate system and anchors match those from the recorded world map.

If ARKit cannot reconcile the recorded world map with the current environment (for example, if the device is in an entirely different place from where the world map was recorded), the session remains in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state indefinitely.

## See Also

- [init()](arworldtrackingconfiguration/init.md)
  Initializes a new world-tracking configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/initialworldmap)*