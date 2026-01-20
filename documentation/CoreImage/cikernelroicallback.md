# CIKernelROICallback

**Framework**: Core Image  
**Kind**: typealias

The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [`apply(extent:roiCallback:arguments:)`](cikernel/apply(extent:roicallback:arguments:).md) method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias CIKernelROICallback = (Int32, CGRect) -> CGRect
```

#### Discussion

The block takes the following parameters:

The block returns a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) structure describing the region of interest for the specified rectangle.

When applying a filter kernel, the region of interest is the area of source image pixels that must be processed to produce a given area of destination image pixels. (For a more detailed definition, see [`The Region of Interest`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12).) For example, a kernel that applies a blur effect in a ten-pixel radius must sample source image pixels ten pixels away in each direction from every output pixel. Thus, its region of interest is a rectangle ten pixels larger on each side than the destination rectangle:

```objc
CIKernelROICallback callback = ^(int index, CGRect rect) {
    return CGRectInset(rect, -10, -10);
};
```

If your kernel does not need the image at `index` to produce output in the rectangle `rect`, your block should return [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull).

## See Also

- [func apply(extent: CGRect, roiCallback: CIKernelROICallback, arguments: [Any]) -> CIImage?](cikernel/apply(extent:roicallback:arguments:).md)
  Creates a new image using the kernel and specified arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernelroicallback)*