# init(_:orientation:physicalWidth:)

**Framework**: ARKit  
**Kind**: init

Creates a new reference image from a Core Graphics image object.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
init(_ image: CGImage, orientation: CGImagePropertyOrientation, physicalWidth: CGFloat)
```

#### Discussion

To accurately recognize the position and orientation of an image in the AR environment, ARKit must know the image’s physical size. When you call this initializer, ARKit uses the `physicalWidth` measurement and `orientation` you provide together with the aspect ratio of the image itself to calculate the physical height. Use the  [`physicalSize`](arreferenceimage/physicalsize.md) property of the created [`ARReferenceImage`](arreferenceimage.md) object to retrieve these values.

> ❗ **Important**: ARKit preprocesses reference images before using them for image detection. To provide reference images bundled with your app, create AR Reference Image assets in your Xcode asset catalog, and use the `referenceImageSetNamed(_:in:)` method to load them.

## Parameters

- `image`: A Core Graphics image object.
- `orientation`: The intended display orientation for the image.
- `physicalWidth`: The real-world width, in meters, of the image.

## See Also

- [init(CVPixelBuffer, orientation: CGImagePropertyOrientation, physicalWidth: CGFloat)](arreferenceimage/init(_:orientation:physicalwidth:)-ir2z.md)
  Creates a new reference image from a Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/init(_:orientation:physicalwidth:)-8b3bs)*