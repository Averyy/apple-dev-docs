# ciContext

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A context for Core Image objects that you can use to render into the graphics context.

**Availability**:
- macOS

## Declaration

```swift
var ciContext: CIContext? { get }
```

```objc
@property (strong, readonly, nullable) CIContext * CIContext;
```

#### Discussion

The [`CIContext`](../../CoreImage/cicontext.md) object is created on demand and remains in existence for the lifetime of its owning [`NSGraphicsContext`](../nsgraphicscontext.md) object. A [`CIContext`](../../CoreImage/cicontext.md) object is an evaluation context for rendering a [`CIImage`](../../CoreImage/ciimage.md) object through Quartz 2D or OpenGL. You use [`CIContext`](../../CoreImage/cicontext.md)` `objects in conjunction with [`CIFilter`](../../CoreImage/cifilter-swift.class.md), [`CIImage`](../../CoreImage/ciimage.md), [`CIVector`](../../CoreImage/civector.md), and [`CIColor`](../../CoreImage/cicolor.md) objects to take advantage of the built-in Core Image filters when processing images.

For more on [`CIContext`](../../CoreImage/cicontext.md) objects and related Core Image objects, see [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/cicontext)*