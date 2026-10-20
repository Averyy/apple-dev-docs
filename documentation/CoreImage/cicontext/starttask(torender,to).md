# startTask(toRender:to:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startTask(toRender image: CIImage, to destination: CIRenderDestination) throws -> CIRenderTask
```

```objc
- (CIRenderTask *) startTaskToRender:(CIImage *) image toDestination:(CIRenderDestination *) destination error:(NSError **) error;
```

#### Return Value

The asynchronous [`CIRenderTask`](../cirendertask.md) to render the image to the specified destination.

## Parameters

- `image`: [`CIImage`](../ciimage.md) to prepare to render.
- `destination`: The [`CIRenderDestination`](../cirenderdestination.md) to which to render.

## See Also

### Customizing Render Destination
- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws](./preparerender%28_,from,to,at%29.md)
  An optional call to warm up a [`CIContext`](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](./starttask%28toclear%29.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](../cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](./starttask%28torender,from,to,at%29.md)
  Renders a portion of an image to a point in the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/starttask(torender:to:))*