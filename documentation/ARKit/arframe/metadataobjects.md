# metadataObjects

**Framework**: ARKit  
**Kind**: property

Metadata objects associated with the current frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var metadataObjects: [AVMetadataObject] { get }
```

#### Discussion

This array contains `AVMetadataFaceObject`s for detected faces when running an `ARFaceTrackingConfiguration` and face tracking is not active (`maximumNumberOfTrackedFaces` set to 0).

> **Note**: [`maximumNumberOfTrackedFaces`](arfacetrackingconfiguration/maximumnumberoftrackedfaces.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/metadataobjects)*