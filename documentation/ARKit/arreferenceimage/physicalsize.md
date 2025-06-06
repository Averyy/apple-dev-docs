# physicalSize

**Framework**: ARKit  
**Kind**: property

The real-world dimensions, in meters, of the image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var physicalSize: CGSize { get }
```

#### Discussion

To accurately recognize the position and orientation of an image in the AR environment, ARKit must know the image’s physical size. You provide this information when creating an AR reference image in your Xcode project’s asset catalog, or when programmatically creating an [`ARReferenceImage`](arreferenceimage.md).

When you want to recognize different-sized versions of a reference image, you set [`automaticImageScaleEstimationEnabled`](arworldtrackingconfiguration/automaticimagescaleestimationenabled.md) to [`true`](https://developer.apple.com/documentation/swift/true), and in this case, ARKit disregards `physicalSize`.

## See Also

- [var name: String?](arreferenceimage/name.md)
  A descriptive name for the image.
- [var resourceGroupName: String?](arreferenceimage/resourcegroupname.md)
  The AR resource group name for this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/physicalsize)*