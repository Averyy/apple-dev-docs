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

The [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) object is created on demand and remains in existence for the lifetime of its owning [`NSGraphicsContext`](nsgraphicscontext.md) object. A [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) object is an evaluation context for rendering a [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage) object through Quartz 2D or OpenGL. You use [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext)` `objects in conjunction with [`CIFilter`](https://developer.apple.com/documentation/coreimage/cifilter), [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage), [`CIVector`](https://developer.apple.com/documentation/coreimage/civector), and [`CIColor`](https://developer.apple.com/documentation/coreimage/cicolor) objects to take advantage of the built-in Core Image filters when processing images.

For more on [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) objects and related Core Image objects, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/cicontext)*