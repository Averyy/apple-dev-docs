# maximumNumberOfTrackedFaces

**Framework**: ARKit  
**Kind**: property

The number of faces to track during the session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var maximumNumberOfTrackedFaces: Int { get set }
```

#### Discussion

The default value is one. Set the maximum number of tracked faces to limit the number of faces that can be tracked in a given frame. Check the value of [`supportedNumberOfTrackedFaces`](arfacetrackingconfiguration/supportednumberoftrackedfaces.md) before setting this property.

No new anchors will be provided to your delegate’s [`session(_:didAdd:)`](arsessiondelegate/session(_:didadd:).md) if more than the maximum number of faces are visible in the camera feed. In that case, ARKit continues to track the faces that already have associated face anchors.

## See Also

- [class var supportedNumberOfTrackedFaces: Int](arfacetrackingconfiguration/supportednumberoftrackedfaces.md)
  The maximum number of faces that the framework can track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacetrackingconfiguration/maximumnumberoftrackedfaces)*