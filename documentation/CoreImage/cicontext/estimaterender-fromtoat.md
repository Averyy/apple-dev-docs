# estimateRender(_:from:to:at:)

**Framework**: Core Image  
**Kind**: method

Returns a task with estimated resource statistics for a render, without executing the render.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func estimateRender(_ image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws -> CIRenderTask
```

#### Return Value

 A [`CIRenderTask`](cirendertask.md) you can query for estimated statistics, or `nil` if `fromRect` doesn’t intersect `image.extent` or if estimation fails.

#### Discussion

Call this method to analyze the cost of a render before you execute it. Query the returned task’s `plannedPixelsProcessed`, `plannedPixelsOverdrawn`, `plannedPassCount`, and `plannedPeakMemory` properties to get the estimated statistics.

The method renders as if the image is cropped to `fromRect` and places the origin of `fromRect` at `atPoint` in the destination.

## Parameters

- `image`: The [`CIImage`](ciimage.md) to estimate the render for.
- `fromRect`: The region of [`CIImage`](ciimage.md) to render.
- `destination`: The [`CIRenderDestination`](cirenderdestination.md) to estimate the render to.
- `atPoint`: The point in the destination where the origin of `fromRect` is placed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/estimaterender(_:from:to:at:))*