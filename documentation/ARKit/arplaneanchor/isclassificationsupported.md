# isClassificationSupported

**Framework**: ARKit  
**Kind**: property

A Boolean value that indicates whether plane classification is available on the current device.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class var isClassificationSupported: Bool { get }
```

#### Discussion

Plane classification is available on iOS devices with A12 or later GPU.

On devices without plane classification support, all plane anchors report a [`classification`](arplaneanchor/classification-2hi2p.md) value of  [`ARPlaneClassificationNone`](arplaneclassification/arplaneclassificationnone.md) and a [`classificationStatus`](arplaneanchor/classificationstatus.md) value of [`ARPlaneClassificationStatusNotAvailable`](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md).

## See Also

- [var classification: ARPlaneAnchor.Classification](arplaneanchor/classification-2r4x8.md)
  A general characterization of what kind of real-world surface the plane anchor represents.
- [ARPlaneAnchor.Classification](arplaneanchor/classification-swift.enum.md)
  Possible characterizations of real-world surfaces represented by plane anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/isclassificationsupported)*