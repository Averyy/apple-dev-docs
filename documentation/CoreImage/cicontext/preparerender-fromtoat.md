# prepareRender(_:from:to:at:)

**Framework**: Core Image  
**Kind**: method

An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func prepareRender(_ image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws
```

#### Discussion

By making this call, the Core Image framework ensures that any needed kernels are compiled, and any intermediate buffers are allocated and marked volatile up front.

## Parameters

- `image`:   to prepare to render.
- `fromRect`: A   defining the region to render.
- `destination`: The   to which you are preparing to render.
- `atPoint`: The   at which you are preparing to render.

## See Also

- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(toclear:).md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](cicontext/starttask(torender:from:to:at:).md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(torender:to:).md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/preparerender(_:from:to:at:))*