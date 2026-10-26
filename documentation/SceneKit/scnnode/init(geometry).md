# init(geometry:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a node object with the specified geometry attached.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init(geometry: SCNGeometry?)
```

```objc
+ (SCNNode *) nodeWithGeometry:(SCNGeometry *) geometry;
```

#### Return Value

A new node object with the geometry attached, or `nil` if initialization is not successful.

## Parameters

- `geometry`: The geometry to be attached.

## See Also

### Creating a Node
- [+ node](./node.md)
  Creates and returns a node object.
- [+ nodeWithMDLObject:](./nodewithmdlobject_.md)
  Creates a node from the specified Model I/O object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/init(geometry:))*