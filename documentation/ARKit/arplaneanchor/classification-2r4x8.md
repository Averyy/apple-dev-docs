# classification

**Framework**: ARKit  
**Kind**: property

A general characterization of what kind of real-world surface the plane anchor represents.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var classification: ARPlaneAnchor.Classification { get }
```

#### Discussion

On supported devices, ARKit automatically attempts to characterize each detected plane, describing it as a real-world surface such as a wall, floor, or table. You can then use this information to enhance the realism of your AR experience; for example, by placing certain virtual content only on floors.

Plane classification can take longer than plane detection, and ARKit reports classifications only for planes where it has a high confidence in the result. If ARKit currently has no classification result for a plane, this property’s value is [`ARPlaneAnchor.Classification.none(_:)`](arplaneanchor/classification-swift.enum/none(_:).md), with an associated [`ARPlaneAnchor.Classification.Status`](arplaneanchor/classification-swift.enum/status.md) value indicating why.

Plane classification is available only on iPhone XS, iPhone XS Max, and iPhone XR. Before using classification results, check the [`isClassificationSupported`](arplaneanchor/isclassificationsupported.md) class property to make sure you’re on a supported device.

## See Also

- [class var isClassificationSupported: Bool](arplaneanchor/isclassificationsupported.md)
  A Boolean value that indicates whether plane classification is available on the current device.
- [ARPlaneAnchor.Classification](arplaneanchor/classification-swift.enum.md)
  Possible characterizations of real-world surfaces represented by plane anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-2r4x8)*