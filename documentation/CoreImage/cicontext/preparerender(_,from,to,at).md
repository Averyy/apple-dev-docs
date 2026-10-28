# prepareRender(_:from:to:at:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

An optional call to warm up a [`CIContext`](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.

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

```objc
- (BOOL) prepareRender:(CIImage *) image fromRect:(CGRect) fromRect toDestination:(CIRenderDestination *) destination atPoint:(CGPoint) atPoint error:(NSError **) error;
```

## Discussion

By making this call, the Core Image framework ensures that any needed kernels are compiled, and any intermediate buffers are allocated and marked volatile up front.

## Parameters

- `image`: [`CIImage`](../ciimage.md) to prepare to render.
- `fromRect`: A [`CGRect`](../../CoreFoundation/cgrect.md) defining the region to render.
- `destination`: The [`CIRenderDestination`](../cirenderdestination.md) to which you are preparing to render.
- `atPoint`: The [`CGPoint`](../../CoreFoundation/cgpoint.md) at which you are preparing to render.

## See Also

### Customizing Render Destination
- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](./starttask%28toclear%29.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](../cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](./starttask%28torender,from,to,at%29.md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) throws -> CIRenderTask](./starttask%28torender,to%29.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/preparerender(_:from:to:at:))*