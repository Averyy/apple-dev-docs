# ARSCNDebugOptionShowWorldOrigin

**Framework**: ARKit  
**Kind**: var  
**Role**: Global Variable

Display a coordinate axis visualization indicating the position and orientation of the AR world coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```c
extern const SCNDebugOptions ARSCNDebugOptionShowWorldOrigin;
```

#### Discussion

This visualization is available to all session configurations and session [`worldAlignment`](./arconfiguration/worldalignment-swift.property.md) options, but is most useful with a [`ARWorldTrackingConfiguration`](./arworldtrackingconfiguration.md) session. For example, if you start running a session when this option is enabled, then take a step backward, the real-world position tracked by the AR world coordinate system should become visible on your device screen.

## See Also

### AR Debugging Overlays
- [ARSCNDebugOptionShowFeaturePoints](./arscndebugoptionshowfeaturepoints.md)
  Display a point cloud showing intermediate results of the scene analysis that ARKit uses to track device position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscndebugoptionshowworldorigin)*