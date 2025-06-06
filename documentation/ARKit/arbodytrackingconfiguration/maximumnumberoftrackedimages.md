# maximumNumberOfTrackedImages

**Framework**: ARKit  
**Kind**: property

The number of image anchors to monitor closely for position and orientation updates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var maximumNumberOfTrackedImages: Int { get set }
```

#### Discussion

When you set a nonzero value for this property, the framework keeps that many image anchors up to date as the session progresses. The framework can track a maximum of four images simultaneously.

The word  in the property name refers to how the framework closely monitors the image’s physical position and orientation for any changes. If the image moves, the framework updates the associated [`ARImageAnchor`](arimageanchor.md) transform with the new pose. ARKit checks for changes every frame.

ARKit tracks the first images it observes in the physical environment from the [`detectionImages`](arbodytrackingconfiguration/detectionimages.md) set. When a session reaches the maximum number of tracked images, the framework attempts to track another member of the set only after one of the existing tracked images leaves the device’s view.

The default value is `0`, which disables image tracking. If you add reference images to [`detectionImages`](arbodytrackingconfiguration/detectionimages.md) with this property set to `0`, ARKit creates image anchors for observed reference images but their positions only update infrequently, such as once every couple of seconds.

## See Also

- [var automaticImageScaleEstimationEnabled: Bool](arbodytrackingconfiguration/automaticimagescaleestimationenabled.md)
  A flag that instructs ARKit to estimate and set the scale of a tracked image on your behalf.
- [var detectionImages: Set<ARReferenceImage>](arbodytrackingconfiguration/detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/maximumnumberoftrackedimages)*