# supportsFrameSemantics(_:)

**Framework**: ARKit  
**Kind**: method

Checks whether a particular feature is supported.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func supportsFrameSemantics(_ frameSemantics: ARConfiguration.FrameSemantics) -> Bool
```

#### Return Value

A boolean value that indicates whether the device supports the argument frame semantics.

#### Discussion

Call this function before attempting to enable a frame semantic on your app’s configuration. For example, if you call `supportsFrameSemantic(.sceneDepth)` on [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md), the function returns [`true`](https://developer.apple.com/documentation/swift/true) on devices that support the LiDAR scanner’s depth buffer.

> ⚠️ **Warning**:  Do not call this function on the superclass, [`ARConfiguration`](arconfiguration.md). Only configuration subclasses support frame semantics, such as those listed in `Choose your session's configuration`.

## Parameters

- `frameSemantics`: The frame semantics for which to check device support.

## See Also

- [var frameSemantics: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.property.md)
  The set of active semantics on the frame.
- [ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct.md)
  Types of optional frame features you can enable in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/supportsframesemantics(_:))*