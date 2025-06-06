# maximumNumberOfTrackedImages

**Framework**: ARKit  
**Kind**: property

The number of image anchors to monitor closely for position and orientation updates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var maximumNumberOfTrackedImages: Int { get set }
```

#### Discussion

When you set a nonzero value for this property, the framework keeps that many image anchors up to date as the session progresses. The framework can track a maximum of four images simultaneously.

The word  in the property name refers to how the framework closely monitors the image’s physical position and orientation for any changes. If the image moves, the framework updates the associated [`ARImageAnchor`](arimageanchor.md) transform with the new pose. ARKit checks for changes every frame.

ARKit tracks the first images it observes in the physical environment from the [`trackingImages`](arimagetrackingconfiguration/trackingimages.md) set. When a session reaches the maximum number of tracked images, the framework attempts to track another member of the set only after one of the existing tracked images leaves the device’s view.

The default value is `1`.

## See Also

- [var trackingImages: Set<ARReferenceImage>](arimagetrackingconfiguration/trackingimages.md)
  A set of images that ARKit searches for and tracks in the user’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arimagetrackingconfiguration/maximumnumberoftrackedimages)*