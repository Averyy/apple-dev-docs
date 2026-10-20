# isClassificationSupported

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether plane classification is available on the current device.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
class var isClassificationSupported: Bool { get }
```

```objc
@property (class, nonatomic, readonly, getter=isClassificationSupported) BOOL classificationSupported;
```

#### Discussion

Plane classification is available on iOS devices with A12 or later GPU.

On devices without plane classification support, all plane anchors report a [`classification`](./classification-2hi2p.md) value of  [`ARPlaneClassificationNone`](../arplaneclassification/arplaneclassificationnone.md) and a [`classificationStatus`](./classificationstatus.md) value of [`ARPlaneClassificationStatusNotAvailable`](../arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md).

## See Also

### Classifying a Plane
- [var classification: ARPlaneAnchor.Classification](./classification-2r4x8.md)
  A general characterization of what kind of real-world surface the plane anchor represents.
- [ARPlaneAnchor.Classification](./classification-swift.enum.md)
  Possible characterizations of real-world surfaces represented by plane anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/isclassificationsupported)*