# ciContext

**Framework**: AppKit  
**Kind**: property

A context for Core Image objects that you can use to render into the graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
var ciContext: CIContext? { get }
```

#### Discussion

The [`CIContext`](https://developer.apple.com/documentation/CoreImage/CIContext) object is created on demand and remains in existence for the lifetime of its owning [`NSGraphicsContext`](nsgraphicscontext.md) object. A [`CIContext`](https://developer.apple.com/documentation/CoreImage/CIContext) object is an evaluation context for rendering a [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) object through Quartz 2D or OpenGL. You use [`CIContext`](https://developer.apple.com/documentation/CoreImage/CIContext)` `objects in conjunction with [`CIFilter`](https://developer.apple.com/documentation/coreimage/cifilter), [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage), [`CIVector`](https://developer.apple.com/documentation/CoreImage/CIVector), and [`CIColor`](https://developer.apple.com/documentation/CoreImage/CIColor) objects to take advantage of the built-in Core Image filters when processing images.

For more on [`CIContext`](https://developer.apple.com/documentation/CoreImage/CIContext) objects and related Core Image objects, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/cicontext)*