# ARWorldMap

**Framework**: ARKit  
**Kind**: class

The state in a world-tracking AR session during which a device maps the user’s position in physical space and proximity to anchor objects.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARWorldMap
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Overview

The session state in a world map includes ARKit’s awareness of the physical space in which the user moves the device. ARKit uses the details of the user’s physical space to determine the device’s position and orientation, as well as any [`ARAnchor`](aranchor.md) objects added to the session that can represent detected real-world features or virtual content placed by your app.

##### Serialize and Deserialize a World Map

When your app quits, you can save the current world map (acquired using [`getCurrentWorldMap(completionHandler:)`](arsession/getcurrentworldmap(completionhandler:).md)). Because [`ARWorldMap`](arworldmap.md) conforms to [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding), you serialize it using [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver).

```swift
func writeWorldMap(_ worldMap: ARWorldMap, to url: URL) throws {
    let data = try NSKeyedArchiver.archivedData(withRootObject: worldMap, requiringSecureCoding: true)
    try data.write(to: url)
}
```

To restore the world map the next time your app launches, use [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver).

```swift
func loadWorldMap(from url: URL) throws -> ARWorldMap {
    let mapData = try Data(contentsOf: url)
    guard let worldMap = try NSKeyedUnarchiver.unarchivedObject(ofClass: ARWorldMap.self, from: mapData)
        else { throw ARError(.invalidWorldMap) }
    return worldMap
}
```

You can use anchors from a resumed world map to place the same virtual content at the same positions from the saved session, if the app launches in the same physical environment.

For more information, see [`Saving and loading world data`](saving-and-loading-world-data.md).

##### Share a Saved World Map

With two devices tracking the same world map, you can build a networked experience in which both users can see and interact with the same virtual content. To send an [`ARWorldMap`](arworldmap.md) to another device:

1. On one device, use [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) to convert the world map to a data object. You don’t need to write the data to a file to send it over the network.
2. Use the networking technology of your choice to send the resulting data to another device. For example, in a [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity) session, call [`send(_:toPeers:with:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/send(_:toPeers:with:)) to send data, and implement [`MCSessionDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate) methods on the other device to receive data.
3. On the receiving device, use [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) to instantiate an [`ARWorldMap`](arworldmap.md) from the data.

For more information, see [`Creating a multiuser AR experience`](creating-a-multiuser-ar-experience.md).

##### Run a Deserialized World Map

To begin a new session from an existing [`ARWorldMap`](arworldmap.md), set a world-tracking configuration’s [`initialWorldMap`](arworldtrackingconfiguration/initialworldmap.md) property and use [`run(_:options:)`](arsession/run(_:options:).md). This starts a new session using the same spatial awareness and anchors loaded from the saved world map.

## Topics

### Examining a World Map
- [var anchors: [ARAnchor]](arworldmap/anchors.md)
  The set of anchors recorded in the world map.
- [var center: simd_float3](arworldmap/center.md)
  The center point of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.
- [var extent: simd_float3](arworldmap/extent.md)
  The size of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.
### Debugging a World Map
- [var rawFeaturePoints: ARPointCloud](arworldmap/rawfeaturepoints.md)
  A coarse representation of the space-mapping data recorded in the world map.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Saving and loading world data](saving-and-loading-world-data.md)
  Serialize a world-tracking session to resume it later on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldmap)*