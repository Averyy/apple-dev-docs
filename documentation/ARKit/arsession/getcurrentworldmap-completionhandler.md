# getCurrentWorldMap(completionHandler:)

**Framework**: ARKit  
**Kind**: method

Returns an object encapsulating the world-tracking session’s space-mapping state and set of anchors.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func currentWorldMap() async throws -> ARWorldMap
```

#### Discussion

An [`ARWorldMap`](arworldmap.md) encapsulates the state of a running [`ARSession`](arsession.md). This state includes ARKit’s awareness of the physical space the user moves the device in (which ARKit uses to determine the device’s position and orientation), as well as any [`ARAnchor`](aranchor.md) objects added to the session (which can represent detected real-world features or virtual content placed by your app). After you use this method to save a session’s world map, you can assign it to a configuration’s [`initialWorldMap`](arworldtrackingconfiguration/initialworldmap.md) property and use [`run(_:options:)`](arsession/run(_:options:).md) to start another session with the same spatial awareness and anchors.

By saving world maps and using them to start new sessions, your app can add new AR capabilities:

-  Create a shared frame of reference by sending archived [`ARWorldMap`](arworldmap.md) objects to a nearby user’s device. With two devices tracking the same world map, you can build a networked experience where both users can see and interact with the same virtual content.
-  Save a world map when your app becomes inactive, then restore it the next time your app launches in the same physical environment. You can use  anchors from the resumed world map to place the same virtual content at the same positions from the saved session.

Before saving a world map, monitor the [`worldMappingStatus`](arframe/worldmappingstatus-swift.property.md) property to verify that ARKit has an adequate understanding of the user’s environment, ensuring that you can reliably make use of the saved map on a different device or at a later time.

World map generation requires a world-tracking AR session. If you call this method on an [`ARSession`](arsession.md) not run with [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md), it invokes your completion handler immediately, providing no world map and an error.

> ❗ **Important**:  ARKit calls your `completionHandler` on the session’s [`delegateQueue`](arsession/delegatequeue.md) (if set; on the main queue otherwise). If you need to perform expensive work from this handler (such as archiving and saving or sending the world map), do so on an appropriate dispatch queue to avoid disrupting performance.

 ARKit calls your `completionHandler` on the session’s [`delegateQueue`](arsession/delegatequeue.md) (if set; on the main queue otherwise). If you need to perform expensive work from this handler (such as archiving and saving or sending the world map), do so on an appropriate dispatch queue to avoid disrupting performance.

## Parameters

- `completionHandler`: A closure to be invoked asynchronously after ARKit finishes generating the world map. The closure takes two parameters:

## See Also

- [Recording and Replaying AR Session Data](recording-and-replaying-ar-session-data.md)
  Record an AR session in Reality Composer and replay it in your ARKit app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/getcurrentworldmap(completionhandler:))*